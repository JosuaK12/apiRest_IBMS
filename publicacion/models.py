from django.db import models
from django.contrib.auth.models import User
from categoria.models import categoria
# Create your models here.

class publicacion(models.Model):
    pub_titulo = models.CharField(max_length=255)
    pub_contenido = models.TextField(max_length=None)
    pub_fechaPublic = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete = models.RESTRICT)
    categoria = models.ForeignKey(categoria , on_delete = models.RESTRICT)
    class Meta:
        verbose_name = "publicacion"
        verbose_name_plural = "Publicaciones"
    def __str__(self):
        return self.pub_titulo
