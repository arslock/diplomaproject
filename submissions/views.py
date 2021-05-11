from django.shortcuts import render

# Create your views here.
from .serializers import SubmitHomeWorkSerializer, SubmitQuizSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SubmitHomeWork, SubmitQuiz
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response


class SubmitHomeWorkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmitHomeWorkSerializer
    parser_classes = (MultiPartParser,)

    queryset = SubmitHomeWork.objects.all()

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