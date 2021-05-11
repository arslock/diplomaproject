from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    main_image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')

    class Meta:
        ordering = ['-created_date']