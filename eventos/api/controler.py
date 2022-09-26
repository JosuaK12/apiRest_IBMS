from ast import Delete
from time import time
from urllib import response
from eventos.models import eventos
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eventos.api import serializable
from registro.models import registro as registroModel
from django.utils import timezone

class getEventos(APIView):
    def get(self,request):
        try:
            eventos = serializable.models.eventos.objects.all().order_by("-eve_fecha")
            date=timezone.now().strftime("%Y-%m-%d")
            time=timezone.now().strftime("%H:%M")
            for eve in eventos:
                if eve.eve_fecha.strftime("%Y-%m-%d")<=date and eve.eve_horaFinal.strftime("%H:%M")<time and eve.eve_estado == "activo":
                    evento = serializable.models.eventos.objects.filter(id=eve.id).update(eve_estado = "finalizado")
                
            serializer = serializable.eventosSerializable(eventos,many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class postEventos(APIView):
    def post(self,request):
        try:
            serializer = serializable.eventosSerializable(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
class putEventos(APIView):
    def put(self,request, id):
        try:
            evento = serializable.models.eventos.objects.get(pk=id)
            serializer = serializable.eventosSerializable(instance=evento,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
class deleteEventos(APIView):
    def delete(self,request, id):
        try:
            date=timezone.now().strftime("%Y-%m-%d")
            evento = serializable.models.eventos.objects.get(pk=id)
            if evento.eve_fecha.strftime("%Y-%m-%d")<date:
                return Response("El evento es pasado no se puede cancelar", status=status.HTTP_400_BAD_REQUEST)
            registro = registroModel.objects.filter(eventos = evento.id)
            if len(registro)>0:
                evento.eve_estado = "cancelado"
                evento.save()
            else:
                evento.delete()
            return Response("Cancelado correctamente",status= status.HTTP_200_OK)    
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)