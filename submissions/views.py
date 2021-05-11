from django.shortcuts import render

# Create your views here.
from .serializers import SubmitQuizSerializer, SubmitClassWorkSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SubmitQuiz, SubmitClassWork
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status


class SubmitClassWorkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmitClassWorkSerializer
    parser_classes = (MultiPartParser,)

    queryset = SubmitClassWork.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   

class SubmitQuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmitQuizSerializer
    parser_classes = (MultiPartParser,)

    queryset = SubmitQuiz.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   