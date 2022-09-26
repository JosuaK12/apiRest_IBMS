from django.db import models
from django.contrib.auth.models import User
from eventos.models import eventos
# Create your models here.

class registro(models.Model):
    reg_fechaRegistro = models.DateField(auto_now_add = True)
    reg_asistencia = models.BooleanField()
    user = models.ForeignKey(User , on_delete = models.RESTRICT)
    eventos = models.ForeignKey(eventos , on_delete = models.RESTRICT)
    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "Registros"
    def __str__(self):
        return self.reg_asistencia
