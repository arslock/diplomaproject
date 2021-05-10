from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

def upload_user_image(instance, filename):
    new_filename = 'avatar' + "." + filename.split('.')[-1]
    return '{}/{}'.format(instance.id, new_filename)


class User(AbstractBaseUser, PermissionsMixin):
    class RoleChoice(models.TextChoices): 
        TEACHER = 'teacher', _('teacher')
        STUDENT = 'student', _('student')

    email = models.EmailField(max_length=70, unique=True)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField()
    cover_image = models.ImageField()

    bio = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role_type = models.CharField(max_length=50, choices=RoleChoice.choices, null=True, blank=True)


    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email


class TeacherUser(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    job_position = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.email
    
class StudentUser(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='students')
    student_grade = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.user.email
