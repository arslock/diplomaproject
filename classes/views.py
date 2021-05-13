from django.shortcuts import render

# Create your views here.
from .serializers import ClassSerializer, ClassWorkSerializer, AnnouncmentSerializer, AboutSerializer, ClassWorkSerializer, UserSerializer, SerializerForImage

from .models import ClassModel, Answer, Announcment, AboutClass, MaterialModel, QuizModel, Question, LessonModel, ClassWork
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from scratchprojecct.tools import HEADER_PARAM, QUERY_CLASS_ID
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from django.contrib.auth import get_user_model
from submissions.models import SubmitClassWork, SubmitQuiz
User = get_user_model()
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet


    

class ClassViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ClassSerializer
    parser_classes = (JSONParser,FormParser,)

    queryset = ClassModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(teacher=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        if self.request.user.role_type == 'student':
            return ClassModel.objects.filter(class_type='public')
        return ClassModel.objects.all()

    @swagger_auto_schema(operation_description="Get announcment of class",
                         manual_parameters=[QUERY_CLASS_ID],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})  
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UploadImageForClass(UpdateModelMixin, GenericViewSet):
    serializer_class = SerializerForImage
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    queryset = ClassModel.objects.all()

class ClassStudentsListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(user_students__id=self.kwargs['class_id'])


class ClassWorkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClassWorkSerializer
    parser_classes = (MultiPartParser,)
    queryset = ClassWork.objects.order_by()
    # prefetch_related(
        # Prefetch(
        #     'class_classwork',
        #     queryset=SubmitClassWork.objects.all(),
        #     to_attr='submited_classwork'
        # ))

    # def get_queryset(self):
    #     return ClassWork.objects.prefetch_related(
    #        Prefetch(
    #         'class_classwork',
    #         queryset=SubmitClassWork.objects.all(),
    #         to_attr='submited_classwork'
    #     )
    #     ).order_by()
    def get_queryset(self):
        extra_kwargs = {}
        if self.request.query_params.get('class'):
            extra_kwargs['scratch_class_id'] = self.request.query_params.get('class')
        return ClassWork.objects.filter(**extra_kwargs)

    @swagger_auto_schema(operation_description="Get classworks of class",
                         manual_parameters=[QUERY_CLASS_ID],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})  
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class AnnouncmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnnouncmentSerializer

    
    def get_queryset(self):
        extra_kwargs = {}
        if self.request.query_params.get('class'):
            extra_kwargs['scratch_class_id'] = self.request.query_params.get('class')
        return Announcment.objects.filter(**extra_kwargs)

    @swagger_auto_schema(operation_description="Get announcment of class",
                         manual_parameters=[QUERY_CLASS_ID],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})  
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)




class AboutClassViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AboutSerializer
    pagination_class = None

    def get_queryset(self):
        extra_kwargs = {}
        if self.request.query_params.get('class'):
            extra_kwargs['scratch_class_id'] = self.request.query_params.get('class')
        return AboutClass.objects.filter(**extra_kwargs)

    @swagger_auto_schema(operation_description="Get about of class",
                         manual_parameters=[QUERY_CLASS_ID],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})  
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

