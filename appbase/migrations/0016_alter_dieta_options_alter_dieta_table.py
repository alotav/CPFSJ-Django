# Generated by Django 4.1 on 2022-09-20 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '000015_alter_dieta_usr_alter_rutina_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dieta',
            options={'ordering': ['id'], 'verbose_name': 'Dieta', 'verbose_name_plural': 'Dietas'},
        ),
        migrations.AlterModelTable(
            name='dieta',
            table='dieta',
        ),
    ]
