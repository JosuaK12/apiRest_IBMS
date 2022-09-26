from ast import GtE
import imp
import re
from tokenize import Token
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registro.api import serializable
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from eventos.api import serializable as eve_serializable

class getRegistro(APIView):
    def get(self,request):
        try:
            registro = serializable.models.registro.objects.all().order_by("id")
            serializer = serializable.registroSerializable(registro,many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class postRegistro(APIView):
    def post(self,request):
        try:
            serializer = serializable.registroSerializable(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
class cambioAsistencia(APIView):
    def put(self,request, id):
        try:
            asistencia = serializable.models.registro.objects.get(pk=id)
            if asistencia.reg_asistencia:
                asistencia.reg_asistencia = False
            else:
                asistencia.reg_asistencia = True
            asistencia.save()
            serializer = serializable.registroSerializable(asistencia)
            return Response (serializer.data,status=status.HTTP_200_OK) 
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
class postRegistroMovil(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            user = request.user.id
            jData = {
                "user_id":user,
                "eventos_id":request.data["eventos_id"]
            }
            serializer = serializable.registroSerializable(data = jData)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
class getRegistroMovil(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user = request.user.id
            date=timezone.now().strftime("%Y-%m-%d")
            registro = serializable.models.registro.objects.filter(user_id = user, reg_asistencia = False, eventos__eve_fecha__gte = date )
            listdata = []
            for con in registro:
                data = {
                    "id":con.id,
                    "eve_nombre":con.eventos.eve_nombre, 
                    "eve_info":con.eventos.eve_info,
                    "eve_fecha":con.eventos.eve_fecha,
                    "eve_horaInicio":con.eventos.eve_horaInicio, 
                    "eve_horaFinal":con.eventos.eve_horaFinal,
                    "eve_estado":con.eventos.eve_estado 
                }
                listdata.append(data)   
            serializer = eve_serializable.eventosSerializable(listdata,many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
