# Generated by Django 4.1.3 on 2022-11-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Contacto', models.CharField(max_length=12)),
                ('Especialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Genero', models.CharField(max_length=10)),
                ('Contacto', models.IntegerField(null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datos', models.TextField()),
                ('tiempo', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctore')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente')),
            ],
        ),
    ]
