from django.shortcuts import render

# Create your views here.
from .models import News
from .serializers import NewsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    queryset = News.objects.all()

    