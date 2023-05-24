# Generated by Django 4.2.1 on 2023-05-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=100)),
                ('contra', models.CharField(max_length=12)),
                ('telefono', models.IntegerField()),
                ('cargo', models.CharField(choices=[('1', 'Encargado ventas'), ('2', 'Administrador de usuarios'), ('3', 'Administrador de cuentas'), ('4', 'Encargado pagina web')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=100)),
                ('contra', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=45)),
                ('region', models.CharField(choices=[('RM', 'Santiago'), ('8', 'VIII Bio-BIo'), ('9', 'IX Araucania')], max_length=2)),
                ('comuna', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vinilo',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('cara_delante', models.FileField(upload_to='files/%Y/%m/%d')),
                ('cara_detras', models.FileField(upload_to='files/%Y/%m/%d')),
                ('nombre_cantante', models.CharField(max_length=40)),
                ('nombre_vinilo', models.CharField(max_length=40)),
                ('estilo', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]