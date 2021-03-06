# Generated by Django 3.1.5 on 2021-01-21 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0007_bet_roi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='lucro',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Retorno'),
        ),
        migrations.CreateModel(
            name='BetUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bets.bet')),
            ],
        ),
    ]
