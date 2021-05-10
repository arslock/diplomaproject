from rest_framework import serializers

from .models import HomeWorkComments, MaterialComments, LessonComments, QuizComments

class HomeWorkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWorkComments
        fields = "__all__"

class MaterialCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialComments
        fields = "__all__"

class LessonCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonComments
        fields = "__all__"

class QuizCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizComments
        fields = "__all__"

