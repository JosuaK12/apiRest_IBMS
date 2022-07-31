from asyncore import read
from rest_framework import serializers
from categoria import models

class categoriaSerializable(serializers.ModelSerializer):

    class Meta:
        model = models.categoria
        fields = "__all__"