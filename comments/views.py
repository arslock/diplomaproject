from django.shortcuts import render

# Create your views here.
from .serializers import ClassWorkCommentSerializer, LessonCommentSerializer, QuizCommentSerializer, MaterialCommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ClassWorkComments, LessonComments, QuizComments, MaterialComments
from rest_framework.generics import ListAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

class ClassWorkCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClassWorkCommentSerializer
    queryset = ClassWorkComments.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LessonCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LessonCommentSerializer
    queryset = LessonComments.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class QuizCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuizCommentSerializer
    queryset = QuizComments.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MaterialCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MaterialCommentSerializer
    queryset = MaterialComments.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ClassWorkComments(ListAPIView):
    permission_classses = (IsAuthenticated,)
    serializer_class = ClassWorkCommentSerializer
    queryset = ClassWorkComments.objects.all()

    def get_queryset(self):
        return ClassWorkComments.objects.filter(classwork=self.kwargs['classwork_id'])

class ClassLessonComments(ListAPIView):
    permission_classses = (IsAuthenticated,)
    serializer_class = LessonCommentSerializer
    queryset = LessonComments.objects.all()

    def get_queryset(self):
        return LessonComments.objects.filter(lesson=self.kwargs['lesson_id'])

class ClassQuizComments(ListAPIView):
    permission_classses = (IsAuthenticated,)
    serializer_class = QuizCommentSerializer
    queryset = QuizComments.objects.all()

    def get_queryset(self):
        return QuizComments.objects.filter(quiz=self.kwargs['quiz_id'])

class ClassMaterialComments(ListAPIView):
    permission_classses = (IsAuthenticated,)
    serializer_class = MaterialCommentSerializer
    queryset = MaterialComments.objects.all()

    def get_queryset(self):
        return MaterialComments.objects.filter(material=self.kwargs['material_id'])


