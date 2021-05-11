from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from .models import User
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserEditSerializer, ProfilePasswordSerializer, UserDetailSerializer, UserRegisterSerializer, UserProfileSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from scratchprojecct.tools import HEADER_PARAM
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework_json_api.pagination import JsonApiPageNumberPagination
from rest_framework.parsers import MultiPartParser

# Create your views here.
class UserRegisterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





class UserProfileView(ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    def get_queryset(self):
        return User.objects.filter(user__id=self.kwargs['user_id'])


# class StudentProfileView(RetrieveAPIView):
#     serializer_class = StudentProfileSerializer
#     permission_classes = (IsAuthenticated,)
#     queryset = StudentUser.objects.all()



class ProfileViewSet(GenericViewSet):
    serializer_class = UserEditSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(operation_description="Get user profile",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})
    def profile(self, request):
        return Response(self.serializer_class(request.user, context={'request': request}).data)

    @swagger_auto_schema(operation_description="Update user profile",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})
    def update(self, request):
        serializer = self.serializer_class(request.user, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ChangePasswordViewSet(GenericViewSet):
    serializer_class = ProfilePasswordSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ''
    
    @swagger_auto_schema(operation_description="Change current user password",
                         manual_parameters=[HEADER_PARAM],
                         responses={200: 'OK', 403: 'Permission denied'})
    def change(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': ['OK']})

class UserListView(ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = JsonApiPageNumberPagination
    queryset = User.objects.all()

    @swagger_auto_schema(operation_description="Get user list",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})
    def get(self, request):
        return super().get(request)


class StudentUserListView(ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = JsonApiPageNumberPagination
    queryset = User.objects.filter(role_type='student')

    @swagger_auto_schema(operation_description="Get user list",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})
    def get(self, request):
        return super().get(request)


class UserUpdateView(UpdateModelMixin, GenericViewSet):
    serializer_class = UserEditSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    
    
    @swagger_auto_schema(operation_description="Update user using put",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    
    @swagger_auto_schema(operation_description="Update user using patch",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class UserDeleteView(DestroyModelMixin, GenericViewSet):
    serializer_class = UserEditSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    @swagger_auto_schema(operation_description="Delete user",
                         manual_parameters=[HEADER_PARAM],
                         responses={201: 'Created', 401: 'Permission denied', 400: 'Bad request body'})  
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)