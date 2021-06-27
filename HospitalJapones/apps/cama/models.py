from django.db import models

class Cama(models.Model):
    id_camaPK = models.AutoField(primary_key=True)
    codigo_cama = models.IntegerField('Nro. Cama',unique=True,blank=False,null=False)
    estado = models.CharField('Estado',max_length=20,blank=False,null=False, default='Desocupada')
    descripcion = models.TextField('Descripción',max_length=500,blank=True,null=True)

    def __str__(self):
        return self.codigo_cama

    class Meta:
        verbose_name = 'Cama'
        verbose_name_plural = 'Camas'
        db_table = 'tb_cama'