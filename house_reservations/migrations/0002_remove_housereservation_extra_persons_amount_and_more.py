# Generated by Django 4.2.6 on 2024-03-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housereservation',
            name='extra_persons_amount',
        ),
        migrations.AddField(
            model_name='housereservation',
            name='total_persons_amount',
            field=models.IntegerField(default=2, verbose_name='Количество человек для проживания в домике'),
            preserve_default=False,
        ),
    ]