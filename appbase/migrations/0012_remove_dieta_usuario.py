# Generated by Django 4.1 on 2022-09-19 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0011_remove_dieta_activacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dieta',
            name='usuario',
        ),
    ]
