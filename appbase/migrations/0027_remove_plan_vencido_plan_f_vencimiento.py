# Generated by Django 4.1 on 2022-09-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0026_remove_plan_restantes_plan_asistencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='vencido',
        ),
        migrations.AddField(
            model_name='plan',
            name='f_vencimiento',
            field=models.DateField(null=True),
        ),
    ]
