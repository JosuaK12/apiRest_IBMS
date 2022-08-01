from django.urls import path
from user.api import controler
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   
from rest_framework.authtoken import views

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("post",controler.postUser.as_view(), name="Crear Usuario"),
    path("get",controler.getUser.as_view(), name="Listar Usuario"),
    path("profile",controler.getProfile.as_view(), name="Perfil"),
    path('api-token-auth/', views.obtain_auth_token)
]
