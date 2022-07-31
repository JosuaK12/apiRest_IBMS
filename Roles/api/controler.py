from Roles.models import Roles
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Roles.api import serializable

class getRoles(APIView):
    def get(self,request):
        try:
            Roles = serializable.models.Roles.objects.all()
            serializer = serializable.RolesSerializable(Roles,many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class postRoles(APIView):
    def post(self,request):
        try:
            serializer = serializable.RolesSerializable(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)
