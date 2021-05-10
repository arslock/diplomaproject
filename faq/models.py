from django.db import models

# Create your models here.
class FAQModel(models.Model):
    question = models.CharField(max_length=355)
    answer = models.TextField()


class ProblemModel(models.Model):
    name = models.CharField(max_length=255)
    problem = models.TextField()