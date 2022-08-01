from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api import serializable
from user.models import extension
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
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
            data = []
            for ext in extension:
                row = [{
                    "id":ext.id,
                    "user_id":ext.user.id,
                    "username":ext.user.username,
                    "first_name":ext.user.first_name,
                    "last_name":ext.user.last_name,
                    "email":ext.user.email,
                    "images":ext.image.url,
                    "roles_id":ext.roles.id,
                    "roles":ext.roles.rol_nombre
                }]
                for a in row:
                    data = data + [a]
            return Response(data , status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
