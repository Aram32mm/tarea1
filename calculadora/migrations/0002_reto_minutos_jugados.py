# Generated by Django 4.1 on 2023-03-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reto',
            name='minutos_jugados',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
