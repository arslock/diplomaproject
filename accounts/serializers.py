from rest_framework import serializers

from .models import User, TeacherUser, StudentUser
import os

from django.core.mail import send_mail




class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'role_type', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, attrs):
        if attrs['confirm_password'] != attrs['password']:
            raise ValidationError({'error': ['Пароли не совпадают']})
        return super().validate(attrs)
    
    def save(self, **kwargs):
        self.validated_data.pop('confirm_password')
        instance = User.objects.create_user(**self.validated_data)
        instance.save()
        return instance

# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'role_type')

#         extra_kwargs = {
#             'password': {
#                 'write_only': True
#             }
#         }

#     def create(self, validated_data):
#         instance = super().create(validated_data)
#         instance.save()
#         return instance


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'bio',
         'avatar', 'cover_image','is_active', 'updated_at', 'date_joined', 'role_type')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'avatar', 'cover_image', 'bio',
        'is_superuser', 'is_staff', 'is_active',  
        'updated_at', 'date_joined', 'role_type')


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserEditSerializer()
    class Meta:
        model = TeacherUser
        fields = "__all__"

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserEditSerializer(many=False)
    class Meta:
        model = StudentUser
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        all_quizes = instance.submited_quizes.exclude(grade=None).values_list('grade', flat=True)
        if (sum(all_quizes) == 0):
            ret['quiz_overall'] = len(all_quizes)
        else: 
            ret['quiz_overall'] = sum(all_quizes) // len(all_quizes)
        all_homeworks = instance.submited_homework.exclude(grade=None).values_list('grade', flat=True)
        if (sum(all_homeworks) == 0):
            ret['homework_overall'] = len(all_homeworks)
        else:
            ret['homework_overall'] = sum(all_homeworks) // len(all_homeworks)
        return ret


class ProfilePasswordSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField()

    class Meta:
        model = User
        fields = ('password', 'password1')

    def validate_password1(self, attrs):
        if self.initial_data['password'] != attrs:
            raise serializers.ValidationError(['Passwords do not match.'])
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password'))
        instance.save()
        return instance

