# Generated by Django 3.1.5 on 2021-01-20 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_bet_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='data',
            field=models.DateTimeField(verbose_name='Data do Evento'),
        ),
    ]