from rest_framework import serializers

from .models import ClassModel, Question, QuizModel, Announcment, Answer, MaterialModel, LessonModel, AboutClass, ClassWork
import string
import random
from django.contrib.auth import get_user_model
# from accounts.models import TeacherUser, User, StudentUser
from submissions.serializers import SubmitQuizSerializer, SubmitClassWorkSerializer
from accounts.models import User
User = get_user_model()

class SerializerForImage(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = ('class_image',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar')

# class TeacherUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = TeacherUser
#         fields = "__all__"

# class ClassTeacherSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = TeacherUser
#         fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class_id = serializers.CharField(read_only=True)
    class Meta:
        model = ClassModel
        fields = '__all__'
        read_only_fields = ('teacher',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['teacher'] = UserSerializer(instance.teacher, context=self.context).data
        return ret



class ClassWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassWork
        fields = '__all__'






class AnnouncmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcment
        fields = "__all__"
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'announcment'
        return ret





class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutClass
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['object_type'] = 'about class'
        return ret



