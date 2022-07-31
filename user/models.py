from django.db import models
from django.contrib.auth.models import User
from Roles.models import Roles 
# Create your models here.

class extension(models.Model):
    user = models.OneToOneField(User , on_delete = models.RESTRICT, unique = True)
    roles = models.ForeignKey(Roles , on_delete = models.RESTRICT)
    image = models.ImageField(upload_to = "users/")
    class Meta:
        verbose_name="extension"
        verbose_name_plural="extensions"
    def __str__(self):
        return self.user.username
