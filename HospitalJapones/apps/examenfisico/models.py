from django.db import models

class ExamenFisico(models.Model):
    id_examenfisicoPK = models.AutoField(primary_key=True)
    tension_arterial = models.CharField('TA',max_length=30,blank=True, null=True, default='-')
    frecuencia_cardiaca = models.CharField('FC',max_length=30,blank=True, null=True, default='-')
    frecuencia_respiratoria = models.CharField('FR',max_length=30,blank=True, null=True, default='-')
    temp_ax = models.CharField('TEMP AX',max_length=30,blank=True, null=True, default='-')
    sindrome_at = models.CharField('SAT',max_length=30,blank=True, null=True, default='-')
    fio = models.CharField('FIO-2',max_length=30,blank=True,null=True, default='-')
    pam = models.CharField('PAM',max_length=30,blank=True,null=True, default='-')
    avm = models.CharField('AVM',max_length=30,blank=True,null=True, default='-')
    modo = models.CharField('MODO',max_length=30,blank=True,null=True, default='-')
    noradrenalina = models.CharField('Noradrenalina',max_length=30,blank=True,null=True, default='-')
    atracurio = models.CharField('Atracurio',max_length=30,blank=True,null=True, default='-')
    vc = models.CharField('VC',max_length=30,blank=True,null=True, default='-')
    peep = models.CharField('PEEP',max_length=30,blank=True,null=True, default='-')
    prono_dias = models.CharField('Prono Días',max_length=30,blank=True,null=True, default='-')
    pao_fio = models.CharField('PAO2/FIO2',max_length=30,blank=True,null=True, default='-')
    pi = models.CharField('PI',max_length=30,blank=True,null=True, default='-')
    peso = models.CharField('Peso',max_length=50,blank=True, null=True, default='-')

    class Meta:
        verbose_name = 'ExamenFisico'
        verbose_name_plural = 'ExamenFisicos'
        db_table = 'tb_examenfisico'