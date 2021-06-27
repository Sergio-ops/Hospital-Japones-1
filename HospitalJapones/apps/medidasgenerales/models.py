from django.db import models

class MedidasGenerales(models.Model):
    id_medidagPK = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=600, blank=True,null=True)
    descripcion = models.CharField(max_length=600, blank=True,null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'MedidaGeneral'
        verbose_name_plural = 'MedidasGenerales'
        db_table = 'tb_medidas_generales'