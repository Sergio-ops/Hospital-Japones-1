from django.db import models
from django.contrib.auth.models import AbstractUser

class Medico(AbstractUser):
    id_medicoPK = models.AutoField(primary_key=True)
    nro_registro = models.IntegerField('Número de Registro',null=True,blank=True,unique=True)
    especialidad = models.CharField('Especialidad',max_length = 200,null=True,blank=True)
    nro_telefono = models.IntegerField('Número de Teléfono',null=True,blank=True)
