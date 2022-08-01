from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from publicacion.api import serializable
from publicacion.models import publicacion
from user.models import extension

class getpublicacion(APIView):
    def get(self,request):
        try:
            data = []
            for publicacion in serializable.models.publicacion.objects.all().order_by("-pub_fechaPublic"):
                G = extension.objects.get(user = publicacion.user)
                rest = [
                    {
                        "id":publicacion.id,
                        "user_id":publicacion.user.id,
                        "user":publicacion.user,
                        "categoria_id":publicacion.categoria.id,
                        "categoria":publicacion.categoria,
                        "pub_titulo":publicacion.pub_titulo,
                        "pub_contenido":publicacion.pub_contenido,
                        "pub_fechaPublic":publicacion.pub_fechaPublic,
                        "image":G.image                      
                    }
                ]
                for E in rest:
                    data += [E]
            serializer = serializable.PublicacionSerializable(data,many = True,context={"request":request})
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class postpublicacion(APIView):
    def post(self,request):
        try:
            serializer = serializable.PublicacionSerializable(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
        except Exception as e:   
            return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR) 