# Generated by Django 4.0.4 on 2022-05-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.CharField(max_length=20, verbose_name='Nit de la empresa'),
        ),
    ]
