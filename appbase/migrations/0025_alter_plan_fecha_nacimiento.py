# Generated by Django 4.1 on 2022-09-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0024_plan_dni_plan_fecha_nacimiento_delete_infousr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
