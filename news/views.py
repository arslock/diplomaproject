from django.shortcuts import render

# Create your views here.
from .models import News
from .serializers import NewsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly 
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from scratchprojecct.tools import QUERY_USER_ID
from drf_yasg.utils import swagger_auto_schema

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser,)
    queryset = News.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        extra_kwargs = {}
        if self.request.query_params.get('id'):
            extra_kwargs['author_id'] = self.request.query_params.get('id')
        return News.objects.filter(**extra_kwargs)

    @swagger_auto_schema(operation_description="Get classworks of class",
                         manual_parameters=[QUERY_USER_ID],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})  
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)