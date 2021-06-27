# Generated by Django 3.2.4 on 2021-06-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_pacientePK', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(max_length=250, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=150, verbose_name='Apellido Materno')),
                ('nro_documento', models.IntegerField(unique=True, verbose_name='Nro de Documento')),
                ('sexo', models.CharField(max_length=2, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('ocupacion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ocupación')),
                ('estado_civil', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado Civil')),
                ('residencia', models.CharField(max_length=150, verbose_name='Residencia')),
                ('procedencia', models.CharField(max_length=150, verbose_name='Procedencia')),
                ('domicilio', models.TextField(blank=True, max_length=600, null=True, verbose_name='Domicilio')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'tb_paciente',
            },
        ),
    ]
