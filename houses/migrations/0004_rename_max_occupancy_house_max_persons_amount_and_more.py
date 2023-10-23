# Generated by Django 4.2.6 on 2023-10-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_housefeature_house_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='max_occupancy',
            new_name='max_persons_amount',
        ),
        migrations.AddField(
            model_name='house',
            name='base_persons_amount',
            field=models.IntegerField(default=2, verbose_name='Базовое количество человек для проживания в домике'),
        ),
        migrations.AddField(
            model_name='house',
            name='price_per_extra_person',
            field=models.IntegerField(default=2000, verbose_name='Цена за дополнительного человека'),
        ),
        migrations.AddField(
            model_name='housereservation',
            name='extra_persons_amount',
            field=models.IntegerField(default=0, verbose_name='Дополнительное количество человек для проживания в домике'),
        ),
    ]