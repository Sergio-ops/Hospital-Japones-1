from django.db import models
from ..indicacion.models import Indicacion
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


class det_solucion(models.Model):
    id_det_solucionPK = models.AutoField(primary_key=True)
    id_solucionFK = models.ForeignKey(Solucion, on_delete=models.CASCADE)
    id_indicacionFK =models.ForeignKey(Indicacion, on_delete=models.CASCADE)
    detalle_indicacion = models.TextField('Indicacion',max_length=200,blank=True,null=True)

    class Meta:
        db_table ="det_solucion_nombresolucion"