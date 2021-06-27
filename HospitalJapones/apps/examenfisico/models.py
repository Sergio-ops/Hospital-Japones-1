from django.db import models

class ExamenFisico(models.Model):
    id_examenfisicoPK = models.AutoField(primary_key=True)
    tension_arterial = models.CharField('TA',max_length=30,blank=True, null=True)
    frecuencia_cardiaca = models.CharField('FC',max_length=30,blank=True, null=True)
    frecuencia_respiratoria = models.CharField('FR',max_length=30,blank=True, null=True)
    temp_ax = models.CharField('TEMP AX',max_length=30,blank=True, null=True)
    sindrome_at = models.CharField('SAT',max_length=30,blank=True, null=True)
    fio = models.CharField('FIO-2',max_length=30,blank=True,null=True)
    pam = models.CharField('PAM',max_length=30,blank=True,null=True)
    avm = models.CharField('AVM',max_length=30,blank=True,null=True)
    modo = models.CharField('MODO',max_length=30,blank=True,null=True)
    noradrenalina = models.CharField('Noradrenalina',max_length=30,blank=True,null=True)
    atracurio = models.CharField('Atracurio',max_length=30,blank=True,null=True)
    vc = models.CharField('VC',max_length=30,blank=True,null=True)
    peep = models.CharField('PEEP',max_length=30,blank=True,null=True)
    prono_dias = models.CharField('Prono Días',max_length=30,blank=True,null=True)
    pao_fio = models.CharField('PAO2/FIO2',max_length=30,blank=True,null=True)
    pi = models.CharField('PI',max_length=30,blank=True,null=True)
    peso = models.CharField('Peso',max_length=50,blank=True, null=True)
    piel_mucosa = models.TextField('Piel y Mucosas',blank=True, null=True)
    neurologico = models.TextField('Neurologico',blank=True, null=True)
    cardiopulmonar = models.TextField('Cardiopulmonar',blank=True, null=True)
    abdomen = models.TextField('Abdomen',blank=True, null=True)
    genitourinario = models.TextField('Genitourinario',blank=True, null=True)
    musculoesqueletico = models.TextField('Musculoesqueletico',blank=True, null=True)

    class Meta:
        verbose_name = 'ExamenFisico'
        verbose_name_plural = 'ExamenFisicos'
        db_table = 'tb_examenfisico'