# Generated by Django 4.0.6 on 2022-07-21 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Roles', '0002_alter_roles_rol_descripcion_alter_roles_rol_nombre'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='roles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Roles.roles', unique=True),
        ),
    ]
