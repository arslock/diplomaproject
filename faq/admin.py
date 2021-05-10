from django.contrib import admin

# Register your models here.
from .models import FAQModel, ProblemModel
admin.site.register(FAQModel)
admin.site.register(ProblemModel)
