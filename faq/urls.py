from django.urls import path, include
from faq import views
from .views import FAQListView, ProblemView

urlpatterns = [
    path('faq/', views.FAQListView.as_view(), name='faq-list'),
    path('problem/', views.ProblemView.as_view(), name='problem-create'),
]