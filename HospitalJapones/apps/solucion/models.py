from django.db import models
from ..nombresolucion.models import NombreSolucion
# Create your models here.
class Solucion(models.Model):
    id_solucionPK = models.AutoField(primary_key=True)
    nombre = models.CharField('Solucion', max_length=150, blank=False, null=False)
    descripcion = models.TextField('Descripcion', blank=False, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Solucion"
        verbose_name_plural = "Soluciones"
        db_table = "tb_solucion"


class det_solucion_nombresolucion(models.Model):
    id_det_solucionPK = models.AutoField(primary_key=True)
    id_solucionFK = models.ForeignKey(Solucion, on_delete=models.CASCADE)
    id_nombresolucionFK =models.ForeignKey(NombreSolucion, on_delete=models.CASCADE)
    fecha = models.DateField('Fecha', blank=True,null=True)

    class Meta:
        db_table ="det_solucion_nombresolucion"