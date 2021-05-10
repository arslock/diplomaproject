from rest_framework import serializers
from .models import SubmitQuiz, SubmitHomeWork
from accounts.models import StudentUser, User

# class SubmitUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'avatar')

# class StudentUserSerializer(serializers.ModelSerializer):
#     user = SubmitUserSerializer()
#     class Meta:
#         model = StudentUser
#         exclude = ['student_grade']

class SubmitQuizSerializer(serializers.ModelSerializer):
    # author = StudentUserSerializer()
    class Meta:
        model = SubmitQuiz
        fields = "__all__"

class SubmitHomeWorkSerializer(serializers.ModelSerializer):
    # author = StudentUserSerializer()
    class Meta:
        model = SubmitHomeWork
        fields = "__all__"

        