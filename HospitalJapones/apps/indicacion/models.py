from django.db import models
from ..solicitudlaboratorio.models import SolicitudLaboratorio
from ..medidasgenerales.models import MedidasGenerales
# Create your models here.
class Indicacion(models.Model):
    id_indicacionPK = models.AutoField(primary_key=True)
    dieta = models.TextField('Dieta',blank=True, null=True )
    terapia_respiratoria = models.TextField('Terapia Respiratoria', blank=True, null=True)

    class  Meta:
        verbose_name = "Indicacion"
        verbose_name_plural = "Indicaciones"
        db_table = "tb_indicacion"


class det_solicitud_indicacion(models.Model):
    id_det_solicitud_indicacionPK = models.AutoField(primary_key=True)
    id_solicitud_laboratioFK = models.ForeignKey(SolicitudLaboratorio, on_delete=models.CASCADE)
    id_indicacionFK = models.ForeignKey(Indicacion, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField('Fecha Solicitud', auto_now=True)

    class Meta:
        db_table = "det_solicitud_indicacion"


class det_indicacion_medida_general(models.Model):
    id_det_indicacion_medidaPK = models.AutoField(primary_key=True)
    id_indicacionFK = models.ForeignKey(Indicacion, on_delete=models.CASCADE)
    id_medida_generalFK = models.ForeignKey(MedidasGenerales, on_delete=models.CASCADE)

    class Meta:
        db_table = "det_indicacion_medida_general"

