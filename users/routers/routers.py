from rest_framework.routers import DefaultRouter
from ..viewsets.users_viewsets import UserViewSet
from django.urls import path

from ..viewsets.users_viewsets import CustomAuthToken 

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('login/', CustomAuthToken.as_view(), name='users-login'),  # 👈 login route
]


