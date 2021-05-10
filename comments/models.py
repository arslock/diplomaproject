from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from classes.models import QuizModel, HomeWorkModel, MaterialModel, LessonModel
# Create your models here.
class QuizComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.comment

class HomeWorkComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    homework = models.ForeignKey(HomeWorkModel, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.comment

class MaterialComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    material = models.ForeignKey(MaterialModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class LessonComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey(LessonModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment