# Generated by Django 4.1.7 on 2023-03-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_compras', '0012_orden_compra_cantidad_orden_compra_costo_unitario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden_compra',
            name='id_asiento',
            field=models.CharField(default='null', max_length=4),
        ),
    ]