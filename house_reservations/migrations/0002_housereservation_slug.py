# Generated by Django 5.0.3 on 2024-05-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='housereservation',
            name='slug',
            field=models.CharField(default='', max_length=64, verbose_name='Строковый идентификатор'),
        ),
    ]
