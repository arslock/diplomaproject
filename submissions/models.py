from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.models import StudentUser
from classes.models import QuizModel, HomeWorkModel
# Create your models here.
class SubmitQuiz(models.Model):
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='submited_quizes')
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='class_quiz')
    grade = models.PositiveIntegerField(null=True, blank=True)
    answer = models.TextField()
    is_late = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

class SubmitHomeWork(models.Model):
    author = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='submited_homework')
    homework = models.ForeignKey(HomeWorkModel, on_delete=models.CASCADE, related_name='class_homework')
    grade = models.PositiveIntegerField(null=True, blank=True)
    uploaded_file = models.FileField()
    is_late = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
