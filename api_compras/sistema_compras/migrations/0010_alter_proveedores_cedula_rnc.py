# Generated by Django 4.1.7 on 2023-03-07 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_compras', '0009_alter_proveedores_cedula_rnc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='cedula_rnc',
            field=models.CharField(max_length=11, verbose_name='Cedula o RNC'),
        ),
    ]
