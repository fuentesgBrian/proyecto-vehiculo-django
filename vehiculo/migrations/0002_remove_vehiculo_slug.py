# Generated by Django 4.0.5 on 2023-07-05 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='slug',
        ),
    ]