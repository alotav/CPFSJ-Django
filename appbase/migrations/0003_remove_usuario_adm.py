# Generated by Django 4.1 on 2022-09-02 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='adm',
        ),
    ]
