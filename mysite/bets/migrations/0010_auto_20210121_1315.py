# Generated by Django 3.1.5 on 2021-01-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0009_delete_betupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='lucro',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Lucro'),
        ),
    ]
