from django.urls import path
from eventos.api import controler

urlpatterns = [
    path("get",controler.getEventos.as_view(), name="listar Eventos"),
    path("post",controler.postEventos.as_view(), name="Crear Eventos"),
    path("put/<id>",controler.putEventos.as_view(), name="Modificar Eventos"),
    path("delete/<id>",controler.deleteEventos.as_view(), name="Eliminar Eventos"),
]