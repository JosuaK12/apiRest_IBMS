# Generated by Django 4.0.6 on 2022-07-22 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_extension_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extension',
            options={'verbose_name': 'extension', 'verbose_name_plural': 'extensions'},
        ),
    ]