from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.models import User
from classes.models import QuizModel, ClassWork
# Create your models here.
class SubmitQuiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submited_quizes')
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='class_quiz')
    grade = models.PositiveIntegerField(null=True, blank=True)
    answer = models.TextField()
    is_late = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

class SubmitClassWork(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submited_classwork')
    homework = models.ForeignKey(ClassWork, on_delete=models.CASCADE, related_name='class_classwork')
    grade = models.PositiveIntegerField(null=True, blank=True)
    uploaded_file = models.FileField()
    is_late = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
