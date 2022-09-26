from django.urls import path
from publicacion.api import controler

urlpatterns = [
    path("get",controler.getpublicacion.as_view(), name="listar Publicacion"),
    path("post",controler.postpublicacion.as_view(), name="Crear Publicacion"),
    path("put/<id>",controler.putPublicacion.as_view(), name="Actualizar Publicacion"),
    path("delete/<id>",controler.deletePublicacion.as_view(), name="Eliminar Publicacion"),
]