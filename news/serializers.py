from rest_framework import serializers
from .models import News
from accounts.models import User

class NewsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar', 'specific_field', 'role_type')

class NewsSerializer(serializers.ModelSerializer):
    author = NewsUserSerializer(read_only=True)
    class Meta:
        model = News
        fields = '__all__'
        # extra_kwargs = {
        #     'author': {'read_only': True}
        # }