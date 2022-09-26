from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from categoria.api import serializable
from categoria.models import categoria

class getCategoria(APIView):
    def get(self,request):
        try:
            categoria = serializable.models.categoria.objects.all()
            serializer = serializable.categoriaSerializable(categoria,many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class postCategoria(APIView):
    def post(self,request):
        try:
            serializer = serializable.categoriaSerializable(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class putCategoria(APIView):
    def put(self,request, id):
        try:
            categoria = serializable.models.categoria.objects.get(pk=id)
            serializer = serializable.categoriaSerializable(instance=categoria,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)