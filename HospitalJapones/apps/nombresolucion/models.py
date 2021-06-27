from django.db import models

class NombreSolucion(models.Model):
    id_nombresolPK = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150,blank=False,null=False)
    descripcion = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'NombreSolucion'
        verbose_name_plural = 'NombreSoluciones'
        db_table = 'tb_nombre_solucion'