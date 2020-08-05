# Generated by Django 3.0.8 on 2020-08-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0005_auto_20200802_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntaFrecuente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=500)),
                ('respuesta', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'PreguntaFrecuente',
                'verbose_name_plural': 'PreguntasFrecuentes',
            },
        ),
    ]
