from django.shortcuts import render

# Create your views here.
from .serializers import SubmitHomeWorkSerializer, SubmitQuizSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SubmitHomeWork, SubmitQuiz
from rest_framework.parsers import MultiPartParser


class SubmitHomeWorkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmitHomeWorkSerializer
    parser_classes = (MultiPartParser,)

    queryset = SubmitHomeWork.objects.all()

class SubmitQuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmitQuizSerializer
    parser_classes = (MultiPartParser,)

    queryset = SubmitQuiz.objects.all()

