from django.urls import path
from registro.api import controler

urlpatterns = [
    path("get",controler.getRegistro.as_view(), name="listar Registro"),
    path("post",controler.postRegistro.as_view(), name="Crear Registro"),
    path("postMovil",controler.postRegistroMovil.as_view(), name="Crear Registro Movil"),
    path("getMovil",controler.getRegistroMovil.as_view(), name="Listar Registro Movil"),
    path("asistencia/<id>",controler.cambioAsistencia.as_view(), name="Cambio Asistencia"),
]