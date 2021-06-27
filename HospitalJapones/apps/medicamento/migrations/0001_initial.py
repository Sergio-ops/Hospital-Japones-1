# Generated by Django 3.2.4 on 2021-06-26 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamentoPK', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Medicamento')),
                ('medida', models.CharField(max_length=100, verbose_name='gr/ml/etc')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
                'db_table': 'tb_medicamento',
            },
        ),
    ]