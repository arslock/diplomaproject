from django.urls import path, include
from .views import ClassViewSet, AnnouncmentViewSet, ClassStudentsListView, ClassWorkViewSet, AboutClassViewSet, UploadImageForClass

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'announcment', AnnouncmentViewSet, basename='AnnouncmentViewSet')
router.register(r'classworkes', ClassWorkViewSet, basename='ClassWorkViewSet')
router.register(r'about', AboutClassViewSet, basename='AnnouncmentViewSet')
router.register(r'class-image', UploadImageForClass)

urlpatterns = [
path('students/<int:class_id>/', ClassStudentsListView.as_view(), name='class-students-list'),
] + router.urls
