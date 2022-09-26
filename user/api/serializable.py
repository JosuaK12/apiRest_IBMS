from email.policy import default
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from user.models import extension,User

class usuarioSerializable(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    images = Base64ImageField(default ='/users/biblia.png',use_url = True , max_length = None)
    rol_id = serializers.IntegerField(default=2)
    roles=serializers.CharField(read_only=True)
    def create(self , validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        instanceExtension = extension()
        instanceExtension.user = instance 
        instanceExtension.roles_id = validate_data.get('rol_id')
        instanceExtension.image = validate_data.get('images')
        instanceExtension.save()
        return instance
    def validate_username(self,data):
        users= User.objects.filter(username=data)
        if len(users)!=0:
            raise serializers.ValidationError({'Error user':'Este nombre de usuario ya esta en uso'})
        else:
            return data
    def validate_email(self,data):
        users= User.objects.filter(email=data)
        if len(users)!=0:
            raise serializers.ValidationError({'Error email':'Este email ya esta en uso'})
        else:
            return data

class usuarioSerializableUpdate(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    rol_id = serializers.IntegerField(default=2)
    roles=serializers.CharField(read_only=True)
    email = serializers.EmailField()

    images = Base64ImageField(default ='/users/biblia.png',use_url = True , max_length = None)
    def update(self , instance, validate_data):
        instance.first_name = validate_data.get('first_name',instance.first_name)
        instance.last_name = validate_data.get('last_name',instance.last_name)
        instance.email = validate_data.get('email',instance.email)
        instance.save()
        instanceExtension = extension.objects.get(user=instance)
        instanceExtension.image = validate_data.get('images',instance.image)
        instanceExtension.roles_id=validate_data.get('rol_id')
        instanceExtension.save()
        return instance
    
    
class listaUser(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    image = serializers.ImageField()
    roles_id = serializers.IntegerField()
    roles = serializers.CharField()

class webLogin(serializers.Serializer):
    username=serializers.CharField(max_length=255)
    password=serializers.CharField(max_length=255)

class JWTToken(serializers.Serializer):
    refresh=serializers.CharField()
    access=serializers.CharField()