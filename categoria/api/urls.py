from django.urls import path
from categoria.api import controler

urlpatterns = [
    path("get",controler.getCategoria.as_view(), name="listar Categoria"),
    path("post",controler.postCategoria.as_view(), name="Crear Categoria"),
]