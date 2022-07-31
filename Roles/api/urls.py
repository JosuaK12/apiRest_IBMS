from django.urls import path
from Roles.api import controler

urlpatterns = [
    path("get",controler.getRoles.as_view(), name="listar Roles"),
    path("post",controler.postRoles.as_view(), name="Crear Roles"),
]
