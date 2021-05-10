from rest_framework import serializers
from .models import FAQModel, ProblemModel
class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQModel
        fields = '__all__'

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemModel
        fields = '__all__'