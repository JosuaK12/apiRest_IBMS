# Generated by Django 4.0.2 on 2022-09-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='eve_estado',
            field=models.CharField(default='activo', max_length=20),
        ),
    ]
