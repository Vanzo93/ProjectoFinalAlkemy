# Generated by Django 5.0.3 on 2024-04-07 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('dni', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.FloatField(max_length=15)),
                ('stock_actual', models.IntegerField(max_length=10)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.proveedor')),
            ],
        ),
    ]
