from django.urls import path
from publicacion.api import controler

urlpatterns = [
    path("get",controler.getpublicacion.as_view(), name="listar Publicacion"),
    path("post",controler.postpublicacion.as_view(), name="Crear Publicacion"),
]