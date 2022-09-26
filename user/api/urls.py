from django.urls import path
from user.api import controler
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   
from rest_framework.authtoken import views

urlpatterns = [
    path('token', controler.WebLogin.as_view(), name='JWT TOKEN'),
    path("post",controler.postUser.as_view(), name="Crear Usuario"),
    path("get",controler.getUser.as_view(), name="Listar Usuario"),
    path("profile",controler.getProfile.as_view(), name="Perfil"),
    path('api-token-auth/', views.obtain_auth_token)
]
