from rest_framework import serializers

from .models import ClassWorkComments, MaterialComments, LessonComments, QuizComments

class ClassWorkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassWorkComments
        fields = "__all__"

        extra_kwargs = {
            'author': {'read_only': True}
        }

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

