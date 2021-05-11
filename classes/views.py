from django.shortcuts import render

# Create your views here.
from .serializers import ClassSerializer, HomeWorkSerializer, AnnouncmentSerializer, \
AnswerSerializer, AboutSerializer, LessonSerializer, MaterialSerializer, QuestionSerializer, QuizSerializer, ClassWorkSerializer, UserSerializer

from .models import ClassModel, HomeWorkModel, Answer, Announcment, AboutClass, MaterialModel, QuizModel, Question, LessonModel
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from scratchprojecct.tools import HEADER_PARAM
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from submissions.models import SubmitHomeWork, SubmitQuiz
User = get_user_model()
from rest_framework.response import Response
from rest_framework import status




class ClassWorkList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClassWorkSerializer
    queryset = ClassModel.objects.prefetch_related(
        Prefetch(
            'lesson_class', 
            queryset=LessonModel.objects.all(),
            to_attr='lesson_list'
        ),
        Prefetch(
            'material_class',
            queryset=MaterialModel.objects.all(),
            to_attr='material_list'
        ),
        Prefetch(
            'homework_class',
            queryset=MaterialModel.objects.all(),
            to_attr='homework_list'
        ),
        Prefetch(
            'quiz_class',
            queryset=QuizModel.objects.all(),
            to_attr='quiz_list',
        ),
        Prefetch(
            'announcment_class',
            queryset=Announcment.objects.all(),
            to_attr='announcment_list'
        )
    ).all()

    def get_queryset(self):
        return ClassModel.objects.prefetch_related(
        Prefetch(
            'lesson_class', 
            queryset=LessonModel.objects.all(),
            to_attr='lesson_list'
        ),
        Prefetch(
            'material_class',
            queryset=MaterialModel.objects.all(),
            to_attr='material_list'
        ),
        Prefetch(
            'homework_class',
            queryset=MaterialModel.objects.all(),
            to_attr='homework_list'
        ),
        Prefetch(
            'quiz_class',
            queryset=QuizModel.objects.all(),
            to_attr='quiz_list',
        ),
        Prefetch(
            'announcment_class',
            queryset=Announcment.objects.all(),
            to_attr='announcment_list'
        )
    ).filter(id=self.kwargs['id'])

class ClassViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClassSerializer
    parser_classes = (MultiPartParser,)

    queryset = ClassModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(teacher=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ClassStudentsListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(students__id=self.kwargs['class_id'])


class HomeWorkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = HomeWorkSerializer
    parser_classes = (MultiPartParser,)
    queryset = HomeWorkModel.objects.prefetch_related(
        Prefetch(
            'class_homework',
            queryset=SubmitHomeWork.objects.all(),
            to_attr='submited_homework_list'
        )
    ).order_by()

class AnnouncmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnnouncmentSerializer
    parser_classes = (MultiPartParser,)
    queryset = Announcment.objects.all()

class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuizSerializer
    queryset = QuizModel.objects.prefetch_related(
        Prefetch(
            'class_quiz',
            queryset=SubmitQuiz.objects.all(),
            to_attr='submited_quizes_list'
        )
    ).order_by()



    

class MaterialViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MaterialSerializer
    parser_classes = (MultiPartParser,)
    queryset = MaterialModel.objects.all()

class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LessonSerializer
    parser_classes = (MultiPartParser,)
    queryset = LessonModel.objects.all()