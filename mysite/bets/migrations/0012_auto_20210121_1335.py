# Generated by Django 3.1.5 on 2021-01-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0011_bet_editar_lucro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='editar_lucro',
            field=models.BooleanField(verbose_name='Editar Lucro'),
        ),
    ]
