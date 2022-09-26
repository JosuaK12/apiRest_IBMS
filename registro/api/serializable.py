from operator import length_hint
from pyexpat import model
from rest_framework import serializers
from registro import models

class registroSerializable(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user = serializers.CharField(read_only=True)
    eventos_id = serializers.IntegerField()
    eventos = serializers.CharField(read_only=True)
    reg_asistencia = serializers.BooleanField(default=False)
    class Meta:
        model = models.registro
        fields = "__all__"
    def validate(self, data):
        registro = models.registro.objects.filter(user_id = data.get("user_id"),eventos_id = data.get("eventos_id"))
        if len(registro)> 0:
            raise serializers.ValidationError({"error":"No se puede registrar dos veces al mismo evento"})
        evento = models.eventos.objects.get(id=data.get("eventos_id"))
        if evento.eve_estado == "cancelado":
            raise serializers.ValidationError({"error":"No se puede registrar a un evento cancelado"})
        return data