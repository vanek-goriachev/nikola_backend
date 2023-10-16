# Generated by Django 4.2.6 on 2023-10-16 17:34

import django.core.validators
from django.db import migrations, models
import houses.models


class Migration(migrations.Migration):
    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='base_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000)],
                                      verbose_name='Базовая цена'),
        ),
        migrations.AlterField(
            model_name='house',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='house',
            name='holidays_multiplier',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)],
                                    verbose_name='Множитель в выходные и праздники'),
        ),
        migrations.AlterField(
            model_name='house',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения'),
        ),
        migrations.AlterField(
            model_name='housepicture',
            name='picture',
            field=models.ImageField(upload_to=houses.models.generate_house_picture_filename),
        ),
    ]
