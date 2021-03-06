# Generated by Django 3.0.8 on 2020-07-28 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CicloLectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(help_text='Inicio del año lectivo')),
                ('fin', models.DateField(help_text='Fin del año lectivo')),
                ('observacion', models.CharField(help_text='Observación sobre el año lectivo', max_length=300)),
            ],
            options={
                'verbose_name': 'Ciclo',
                'verbose_name_plural': 'Ciclos',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('ciclo_lectivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institucion.CicloLectivo')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Paralelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institucion.Curso')),
            ],
            options={
                'verbose_name': 'Paralelo',
                'verbose_name_plural': 'Paralelos',
            },
        ),
        migrations.CreateModel(
            name='InstitucionCicloLectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo_lectivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institucion.CicloLectivo')),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institucion.Institucion')),
            ],
            options={
                'verbose_name': 'InstitucionCicloLectivo',
                'verbose_name_plural': 'InstitucionesCiclosLectivos',
            },
        ),
    ]
