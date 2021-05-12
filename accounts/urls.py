from .views import (UserRegisterViewSet, ProfileViewSet, ChangePasswordViewSet, UserListView, StudentUserListView,UserUpdateView, UserDeleteView, UserProfileView)
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

router = DefaultRouter()
router.register(r'register', UserRegisterViewSet)
router.register(r'update', UserUpdateView)
router.register(r'delete', UserDeleteView)

urlpatterns = [

path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

path('profile/', ProfileViewSet.as_view({'get': 'profile', 'put': 'update'})),
# path('student-profile/<int:pk>', UserProfileView.as_view()),
path('user-profile/<int:user_id>', UserProfileView.as_view()),
path('change/password/', ChangePasswordViewSet.as_view({'post': 'change'})),
path('user-list/', UserListView.as_view()),
path('student-list/', StudentUserListView.as_view()),
] + router.urls

