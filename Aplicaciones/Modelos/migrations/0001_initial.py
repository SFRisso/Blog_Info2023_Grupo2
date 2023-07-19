# Generated by Django 4.2.3 on 2023-07-18 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.CharField(max_length=1000)),
                ('localidad', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('imagen_portada', models.CharField(max_length=250)),
                ('modalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('foto_perfil', models.CharField(max_length=250)),
                ('tipo_usuario', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateField()),
                ('fecha_edicion', models.DateField()),
                ('contenido', models.CharField(max_length=500)),
                ('id_articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Modelos.articulo')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Modelos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('id_articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Modelos.articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Modelos.categoria'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Modelos.usuario'),
        ),
    ]
