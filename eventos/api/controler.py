from eventos.models import eventos
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eventos.api import serializable

class getEventos(APIView):
    def get(self,request):
        try:
            eventos = serializable.models.eventos.objects.all()
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