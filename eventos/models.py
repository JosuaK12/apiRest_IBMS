from tabnanny import verbose
from django.db import models

# Create your models here.

class eventos(models.Model):
    eve_nombre = models.CharField(max_length= 255)
    eve_info = models.CharField(max_length=255)
    eve_fecha = models.DateField()
    eve_horaInicio = models.TimeField()
    eve_horaFinal = models.TimeField()
    
    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "Eventos"
    def __str__(self):
        return self.eve_nombre
