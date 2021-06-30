# Generated by Django 3.2.4 on 2021-06-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaclinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historiaclinica',
            options={'ordering': ['id_historiaPK'], 'verbose_name': 'HistoriaClinica', 'verbose_name_plural': 'HistoriaClinicas'},
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='abdomen',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Abdomen'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='cardiopulmonar',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Cardiopulmonar'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='frecuencia_cardiaca',
            field=models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='FC'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='frecuencia_respiratoria',
            field=models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='FR'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='genitourinario',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Genitourinario'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='musculoesqueletico',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Musculoesqueletico'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='neurologico',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Neurologico'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='peso',
            field=models.CharField(blank=True, default='-', max_length=50, null=True, verbose_name='Peso'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='piel_mucosa',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Piel y Mucosas'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='sindrome_at',
            field=models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='SAT'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='temp_ax',
            field=models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='TEMP AX'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='tension_arterial',
            field=models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='TA'),
        ),
    ]
