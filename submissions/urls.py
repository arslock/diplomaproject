from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SubmitQuizViewSet, SubmitClassWorkViewSet

router = DefaultRouter()
router.register(r'submit-classwork', SubmitClassWorkViewSet)
# router.register(r'submit-quiz', SubmitQuizViewSet)

urlpatterns = [

] + router.urls