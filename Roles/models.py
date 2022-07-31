from django.db import models

# Create your models here.

class Roles(models.Model):
    rol_nombre = models.CharField(max_length= 255)
    rol_descripcion = models.CharField(max_length=255)
    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "Roles"
    def __str__(self):
        return self.rol_nombre