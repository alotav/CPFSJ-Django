# Generated by Django 4.1 on 2022-10-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbase', '0030_rutinasemanal'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutinasemanal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rutinasemanal',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]