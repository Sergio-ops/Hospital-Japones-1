from django.db import models
from ..medicamento.models import Medicamento
# Create your models here.
class TratamientoIndicacion(models.Model):
    id_tratamientoindicacionPK = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre Tratamiento', max_length=50, blank=False, null=False)
    descripcion = models.TextField('Descripcion Indicacion', blank=False, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "TratamientoIndicacion"
        verbose_name_plural = "TratamientoIndicaciones"
        db_table = "tb_tratamiento_indicacion"

    
class det_tratamiento_indicacion(models.Model):
    id_det_tratamiento_indicacionPK = models.AutoField(primary_key=True)
    id_tratamiento_indicacionFK = models.ForeignKey(TratamientoIndicacion, on_delete=models.CASCADE)
    id_medicamentoFK =models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad', blank=False, null=False)

    class Meta:
        db_table = "det_tratamiento_indicacion"