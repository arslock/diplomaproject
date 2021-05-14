from rest_framework import serializers

from .models import ClassWorkComments, MaterialComments, LessonComments, QuizComments
from accounts.models import User

class CommentAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar', 'specific_field', 'role_type')

class ClassWorkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassWorkComments
        fields = "__all__"
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['author'] = CommentAuthorSerializer(instance.author, context=self.context).data
        return ret




















class MaterialCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialComments
        fields = "__all__"
        extra_kwargs = {
            'author': {'read_only': True}
        }

class LessonCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonComments
        fields = "__all__"
        extra_kwargs = {
            'author': {'read_only': True}
        }

class QuizCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizComments
        fields = "__all__"
        extra_kwargs = {
            'author': {'read_only': True}
        }

