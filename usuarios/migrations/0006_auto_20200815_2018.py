# Generated by Django 3.0.8 on 2020-08-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20200806_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
