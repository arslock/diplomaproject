from django.contrib import admin
from .models import User, TeacherUser, StudentUser

class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'is_staff', 'is_active', 'role_type')

admin.site.register(User, UserAdmin)
admin.site.register(TeacherUser)
admin.site.register(StudentUser)

