from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api import serializable
from user.models import extension
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.hashers import check_password
class postUser(APIView):
    def post(self,request):
        try:
            serializer = serializable.usuarioSerializable(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Registrado correctamente", status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class updateUser(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication,TokenAuthentication]
    def put(self,request,id):
        try:
            user=serializable.User.objects.get(pk=id)
            serializer=serializable.usuarioSerializableUpdate(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Actualizado Correctamente",status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class getUser(APIView):
    def get(self, request):
        try:
            extension = serializable.extension.objects.all()
            data = []
            for ext in extension:
                row = [{
                    "id":ext.id,
                    "user_id":ext.user.id,
                    "username":ext.user.username,
                    "first_name":ext.user.first_name,
                    "last_name":ext.user.last_name,
                    "email":ext.user.email,
                    "image":ext.image,
                    "roles_id":ext.roles.id,
                    "roles":ext.roles.rol_nombre
                }]
                for a in row:
                    data = data + [a]
            serialize = serializable.listaUser(data, many = True, context = {"request":request})
            return Response(serialize.data , status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
class getProfile(APIView):
    authentication_classes = [JWTAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            extension = serializable.extension.objects.filter(user = request.user.id )
            row={}
            for ext in extension:
                row = {
                    "id":ext.id,
                    "user_id":ext.user.id,
                    "username":ext.user.username,
                    "first_name":ext.user.first_name,
                    "last_name":ext.user.last_name,
                    "email":ext.user.email,
                    "image":ext.image,
                    "roles_id":ext.roles.id,
                    "roles":ext.roles.rol_nombre
                }
            serializer=serializable.listaUser(row,context={"request":request})
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class WebLogin(APIView):
    def post(self,request):
        try:
            serializer=serializable.webLogin(data=request.data)
            if serializer.is_valid():
                if serializable.User.objects.filter(username=serializer.data["username"]).exists():
                    user=serializable.User.objects.get(username=serializer.data["username"])
                    ext=serializable.extension.objects.get(user=user)
                    if ext.roles_id==2:
                        return Response({"non_field_errors":["No tienes los permisos para acceder"]},status= status.HTTP_401_UNAUTHORIZED)
                    if check_password(serializer.data["password"],user.password):
                        refresh = RefreshToken.for_user(user)
                        tok={
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        }
                        tokserial=serializable.JWTToken(tok)
                        return Response(tokserial.data,status=status.HTTP_200_OK)
                    return Response({"non_field_errors":["No puede iniciar sesion con las credenciales proporcionadas"]},status= status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"non_field_errors":["No puede iniciar sesion con las credenciales proporcionadas"]},status= status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)