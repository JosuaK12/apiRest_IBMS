from rest_framework import serializers
from registro import models

class registroSerializable(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user = serializers.CharField(read_only=True)
    eventos_id = serializers.IntegerField()
    eventos = serializers.CharField(read_only=True)
    class Meta:
        model = models.registro
        fields = "__all__"