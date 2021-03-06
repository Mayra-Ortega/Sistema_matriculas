# Generated by Django 3.0.8 on 2020-07-28 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0002_ciclolectivo_curso_institucionciclolectivo_paralelo'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioCicloLectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo_lectivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institucion.CicloLectivo')),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Estudiante')),
            ],
            options={
                'verbose_name': 'UsuarioCicloLectivo',
                'verbose_name_plural': 'UsuariosCicloLectivo',
            },
        ),
    ]
