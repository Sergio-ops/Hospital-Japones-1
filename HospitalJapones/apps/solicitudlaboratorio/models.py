from django.db import models

class SolicitudLaboratorio(models.Model):
    id_solicitudlabPK = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'SolicitudLab'
        verbose_name_plural = 'SolicitudLabs'
        db_table = 'tb_solicitudlab'