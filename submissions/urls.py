from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SubmitHomeWorkViewSet, SubmitQuizViewSet

router = DefaultRouter()
router.register(r'submit-hw', SubmitHomeWorkViewSet)
router.register(r'submit-quiz', SubmitQuizViewSet)

urlpatterns = [

] + router.urls