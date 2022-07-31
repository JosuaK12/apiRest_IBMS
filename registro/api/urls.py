from django.urls import path
from registro.api import controler

urlpatterns = [
    path("get",controler.getRegistro.as_view(), name="listar Registro"),
    path("post",controler.postRegistro.as_view(), name="Crear Registro"),
]