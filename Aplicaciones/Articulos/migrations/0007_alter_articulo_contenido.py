# Generated by Django 4.2.3 on 2023-07-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0006_alter_articulo_imagen_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(),
        ),
    ]
