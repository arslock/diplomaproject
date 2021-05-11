from django.urls import path, include
from .views import ClassViewSet, AnnouncmentViewSet, ClassStudentsListView, QuizViewSet, MaterialViewSet, LessonViewSet, HomeWorkViewSet, ClassWorkList, AboutClassViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'announcment', AnnouncmentViewSet, basename='AnnouncmentViewSet')
router.register(r'quiz', QuizViewSet)
router.register(r'material', MaterialViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'homework', HomeWorkViewSet)
router.register(r'about', AboutClassViewSet, basename='AnnouncmentViewSet')

urlpatterns = [
path('students/<int:class_id>/', ClassStudentsListView.as_view(), name='class-students-list'),
path('classwork/<pk>/', ClassWorkList.as_view(), name='class-work-list'),
] + router.urls
