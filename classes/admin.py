from django.contrib import admin

# Register your models here.
from .models import ClassModel, ClassWork, AboutClass, Announcment

admin.site.register(ClassModel)
admin.site.register(ClassWork)

admin.site.register(Announcment)




