# Generated by Django 3.1.5 on 2021-01-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0003_auto_20210120_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='data',
            field=models.DateField(verbose_name='Data do Evento'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='evento',
            field=models.CharField(max_length=50, verbose_name='Nome do Evento'),
        ),
    ]
