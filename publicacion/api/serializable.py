from rest_framework import serializers
from categoria.models import categoria
from publicacion import models

class PublicacionSerializable(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user = serializers.CharField(read_only=True)
    categoria_id = serializers.IntegerField()
    categoria = serializers.CharField(read_only=True)
    class Meta:
        model = models.publicacion
        fields = "__all__"