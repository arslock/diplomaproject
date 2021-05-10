from django.shortcuts import render

# Create your views here.
from .models import FAQModel, ProblemModel

from .serializers import FaqSerializer, ProblemSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

class FAQListView(ListAPIView):
    serializer_class = FaqSerializer
    permission_classes = (IsAuthenticated,)
    queryset = FAQModel.objects.all()

class ProblemView(CreateAPIView):
    serializer_class = ProblemSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ProblemModel.objects.all()

    