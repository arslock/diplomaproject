from django.urls import path, include
from .views import ClassViewSet, AnnouncmentViewSet, ClassStudentsListView, QuizViewSet, MaterialViewSet, LessonViewSet, HomeWorkViewSet, ClassWorkList

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'announcment', AnnouncmentViewSet)
router.register(r'quiz', QuizViewSet)
router.register(r'material', MaterialViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'homework', HomeWorkViewSet)

urlpatterns = [
path('students/<int:class_id>', ClassStudentsListView.as_view(), name='class-students-list'),
path('classwork/<int:id>', ClassWorkList.as_view(), name='class-work-list'),
] + router.urls
