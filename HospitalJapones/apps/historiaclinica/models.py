from datetime import timezone
from django.db import models
from ..medico.models import Medico
from ..paciente.models import Paciente

class HistoriaClinica(models.Model):
    id_historiaPK = models.AutoField(primary_key=True)
    id_medicoFK = models.ForeignKey(Medico, on_delete=models.CASCADE)
    id_pacienteFK = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cod_historiaclinica = models.IntegerField('HC',blank=False,null=False)
    fecha_ingresohospital = models.DateTimeField('Fecha de ingreso a Hospital',blank=False,null=False)
    fecha_ingresodomo = models.DateTimeField('Fecha de ingreso a Domo',blank=True,null=True)
    grado_instruccion = models.CharField('Grado Instrucción',max_length=100, blank=False,null=False)
    proviene = models.CharField('Proviene de',max_length=100,blank=False,null=False)
    antecedente = models.CharField('Antecedentes', max_length=700,blank=False,null=False)
    historia_enfermedad_actual = models.TextField('Historia de la Enfermedad Actual',blank=False,null=False)
    impresion_diagnostica = models.TextField('Impresion Diagnostica',blank=False,null=False)

    def __str__(self):
        return str(self.cod_historiaclinica)

    class Meta:
        verbose_name = 'HistoriaClinica'
        verbose_name_plural = 'HistoriaClinicas'
        db_table = 'tb_historiaclinica'