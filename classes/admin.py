from django.contrib import admin

# Register your models here.
from .models import ClassModel, HomeWorkModel, QuizModel, MaterialModel, Question, Answer, LessonModel, AboutClass, Announcment

admin.site.register(ClassModel)
admin.site.register(HomeWorkModel)
admin.site.register(QuizModel)
admin.site.register(MaterialModel)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Announcment)




