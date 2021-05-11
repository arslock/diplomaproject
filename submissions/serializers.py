from rest_framework import serializers
from .models import SubmitQuiz, SubmitHomeWork
from accounts.models import User

# class SubmitUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'avatar')

# class StudentUserSerializer(serializers.ModelSerializer):
#     user = SubmitUserSerializer()
#     class Meta:
#         model = StudentUser
#         exclude = ['student_grade']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar', 'specific_field')

class SubmitQuizSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = SubmitQuiz
        fields = "__all__"
        extra_kwargs = {
                'author': {'read_only': True}
            }

class SubmitHomeWorkSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = SubmitHomeWork
        fields = "__all__"
        extra_kwargs = {
                'author': {'read_only': True}
            }
            