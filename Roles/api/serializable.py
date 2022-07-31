from rest_framework import serializers
from Roles import models

class RolesSerializable(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = "__all__"
