# Generated by Django 4.2.3 on 2023-07-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0005_alter_articulo_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen_portada',
            field=models.ImageField(upload_to='portada'),
        ),
    ]
