from django.urls import path, include
from .views import ClassViewSet, AnnouncmentViewSet, ClassStudentsListView, ClassWorkViewSet, AboutClassViewSet,\
     UploadImageForClass, StudentsClasses, ClassesWhereNot

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'announcment', AnnouncmentViewSet, basename='AnnouncmentViewSet')
router.register(r'classworkes', ClassWorkViewSet, basename='ClassWorkViewSet')
# router.register(r'about', AboutClassViewSet, basename='AnnouncmentViewSet')
router.register(r'class-image', UploadImageForClass)

urlpatterns = [
path('students/<int:class_id>/', ClassStudentsListView.as_view(), name='class-students-list'),
path('student-classes/', StudentsClasses.as_view(), name='student-classes'),
path('student-not/', ClassesWhereNot.as_view(), name='classes-where-student-not-signed')
] + router.urls
