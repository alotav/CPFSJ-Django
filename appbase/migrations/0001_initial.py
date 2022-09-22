# Generated by Django 4.1 on 2022-08-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nacimiento', models.DateField()),
                ('pago', models.DateField()),
                ('vencido', models.BooleanField()),
                ('plan', models.CharField(max_length=4)),
                ('adm', models.BooleanField()),
            ],
        ),
    ]
