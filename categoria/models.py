from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class categoria(models.Model):
    cat_nombre = models.CharField(max_length=255)
    cat_descripcion = models.CharField(max_length=255)
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.cat_nombre