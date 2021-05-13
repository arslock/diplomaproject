from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# from accounts.models import TeacherUser, StudentUser
User = get_user_model()
import os

# Create your models here.
class ClassModel(models.Model):
    class ClassType(models.TextChoices): 
        PRIVATE = 'private', _('private')
        PUBLIC = 'public', _('public')

    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_teacher')
    students = models.ManyToManyField(User, related_name='user_students', blank=True)
    class_type = models.CharField(max_length=50, choices=ClassType.choices)
    class_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    class_id = models.CharField(max_length=10)
    class_image = models.ImageField(blank=True, null=True)

    syllabus = models.JSONField(blank=True, null=True)
    about_course = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.class_name
    
    

class LessonModel(models.Model):
    scratch_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='lesson_class')
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    uploaded_file = models.FileField()



    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class MaterialModel(models.Model):
    scratch_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='material_class')

    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    uploaded_file = models.FileField()

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

class ClassWork(models.Model):
    class ClassWorkChoice(models.TextChoices): 
        LESSON = 'lesson', _('lesson')
        MATERIAL = 'material', _('material')
        HOMEWORK = 'homework', _('homework')

    scratch_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='class_work')

    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    uploaded_file = models.FileField()
    due_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    classwork_type = models.CharField(max_length=50, choices=ClassWorkChoice.choices)

    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def file_size(self):
        return os.path.getsize('media/'+str(self.uploaded_file))

class QuizModel(models.Model):
    scratch_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='quiz_class')
    title = models.CharField(max_length=250)
    subtitle = models.TextField()
    is_active = models.BooleanField(default=True)
    questions = models.ManyToManyField('Question')

    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=500, verbose_name='Вопрос', blank=True, null=True)

    class QuestionType(models.TextChoices):
        TEXT = 'text', _('text')
        CHECK_BOX = 'check box', _('check box')
        MULTIPLE_CHOICE = 'multiple choice', _('multiple choice')
    
    question_type = models.CharField(max_length=50, choices=QuestionType.choices, verbose_name='Тип вопроса', null=True, blank=True)
    answers = models.ManyToManyField('Answer', null=True, blank=True)

    def __str__(self):
        return self.question

   

class Answer(models.Model):
    answer = models.CharField(max_length=250)
    def __str__(self):
        return self.answer

    
    

class Announcment(models.Model):
    scratch_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='announcment_class')
    annoucment_text = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class AboutClass(models.Model):
    scratch_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='about_class')

    class LanguageType(models.TextChoices): 
        ENGLISH = 'english', _('english')
        RUSSIAN = 'russian', _('russian')
        KAZAKH = 'kazakh', _('kazakh')

    language_type = models.CharField(max_length=50, choices=LanguageType.choices)
    syllabus = models.JSONField()
    about_course = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


