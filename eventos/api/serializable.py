from rest_framework import serializers
from eventos import models

class eventosSerializable(serializers.ModelSerializer):
    class Meta:
        model = models.eventos
        fields = "__all__"