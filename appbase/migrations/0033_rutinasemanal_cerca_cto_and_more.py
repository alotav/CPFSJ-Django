# Generated by Django 4.1 on 2022-10-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0032_rutinasemanal_f_vencimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutinasemanal',
            name='cerca_cto',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rutinasemanal',
            name='f_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
