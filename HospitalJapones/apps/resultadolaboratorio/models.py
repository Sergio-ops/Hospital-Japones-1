from django.db import models

class ResultadoLab(models.Model):
    id_resultadolabPK = models.AutoField(primary_key=True)
    lab_gb = models.CharField('GB',max_length=20,blank=True,null=True, default='-')
    lab_hb = models.CharField('HB',max_length=20,blank=True,null=True, default='-')
    lab_ph = models.CharField('PH',max_length=20,blank=True,null=True, default='-')
    lab_got = models.CharField('GOT',max_length=20,blank=True,null=True, default='-')
    lab_neu = models.CharField('NEU',max_length=20,blank=True,null=True, default='-')
    lab_htco = models.CharField('HTCO',max_length=20,blank=True,null=True, default='-')
    lab_pco = models.CharField('PCO2',max_length=20,blank=True,null=True, default='-')
    lab_gpt = models.CharField('GPT',max_length=20,blank=True,null=True, default='-')
    lab_lin = models.CharField('LIN',max_length=20,blank=True,null=True, default='-')
    lab_cr = models.CharField('CR',max_length=20,blank=True,null=True, default='-')
    lab_hco = models.CharField('HCO3',max_length=20,blank=True,null=True, default='-')
    lab_pt = models.CharField('PT',max_length=20,blank=True,null=True, default='-')
    lab_cay = models.CharField('CAY',max_length=20,blank=True,null=True, default='-')
    lab_urea = models.CharField('UREA',max_length=20,blank=True,null=True, default='-')
    lab_alb = models.CharField('ALB',max_length=20,blank=True,null=True, default='-')
    lab_po = models.CharField('PO2',max_length=20,blank=True,null=True, default='-')
    lab_plq = models.CharField('PLQ',max_length=20,blank=True,null=True, default='-')
    lab_na = models.CharField('NA',max_length=20,blank=True,null=True, default='-')
    lab_eb = models.CharField('EB',max_length=20,blank=True,null=True, default='-')
    lab_cl = models.CharField('CL',max_length=20,blank=True,null=True, default='-')
    lab_k = models.CharField('K',max_length=20,blank=True,null=True, default='-')
    lab_lact = models.CharField('LACT',max_length=20,blank=True,null=True, default='-')
    lab_dd = models.CharField('DD',max_length=20,blank=True,null=True, default='-')

    class Meta:
        verbose_name = 'Resultadolab'
        verbose_name_plural = 'Resultadolabs'
        db_table = 'tb_resultadolab'
