# Generated by Django 5.0.3 on 2024-03-17 00:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('house_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housereservationbill',
            name='reservation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill', to='house_reservations.housereservation', verbose_name='Счет на оплату бронирования домика'),
        ),
    ]