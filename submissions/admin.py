from django.contrib import admin

# Register your models here.
from .models import SubmitHomeWork, SubmitQuiz

admin.site.register(SubmitHomeWork)
admin.site.register(SubmitQuiz)