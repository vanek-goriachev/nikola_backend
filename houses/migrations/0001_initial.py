# Generated by Django 4.2.6 on 2023-10-18 21:03

import django.contrib.postgres.constraints
import django.contrib.postgres.fields.ranges
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import houses.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название домика')),
                ('description', models.TextField(verbose_name='Описание домика')),
                ('max_occupancy', models.IntegerField(default=3, verbose_name='Максимальное количество человек для проживания в домике')),
                ('base_price', models.IntegerField(default=10000, validators=[django.core.validators.MinValueValidator(5000, message='Базовая цена домика должна быть не меньше, чем 5000')], verbose_name='Базовая цена')),
                ('holidays_multiplier', models.FloatField(default=2, validators=[django.core.validators.MinValueValidator(1, message='Множитель в выходные дни должен быть не меньше, чем 1')], verbose_name='Множитель в выходные и праздники')),
                ('closed', models.BooleanField(default=False, verbose_name='Домик закрыт на ремонт?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания домика')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения домика')),
            ],
            options={
                'verbose_name': 'Домик',
                'verbose_name_plural': 'Домики',
            },
        ),
        migrations.CreateModel(
            name='HouseReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_datetime', models.DateTimeField(verbose_name='Дата и время заезда')),
                ('check_out_datetime', models.DateTimeField(verbose_name='Дата и время выезда')),
                ('price', models.IntegerField(blank=True, verbose_name='Стоимость')),
                ('preferred_contact', models.CharField(max_length=255, verbose_name='Предпочтительный способ связи')),
                ('comment', models.CharField(max_length=511, verbose_name='Комментарий')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Отменено?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания домика')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения домика')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservations', to='clients.client')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservations', to='houses.house')),
            ],
            options={
                'verbose_name': 'Бронь домика',
                'verbose_name_plural': 'Брони домиков',
            },
        ),
        migrations.CreateModel(
            name='HousePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=houses.models.generate_house_picture_filename, verbose_name='Путь до файла с изображением')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pictures', to='houses.house', verbose_name='Домик')),
            ],
            options={
                'verbose_name': 'Изображение домика',
                'verbose_name_plural': 'Изображения домиков',
            },
        ),
        migrations.AddConstraint(
            model_name='housereservation',
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(condition=models.Q(('cancelled', False), ('house', None), _connector='OR'), expressions=[(houses.models.TsTzRange('check_in_datetime', 'check_out_datetime', django.contrib.postgres.fields.ranges.RangeBoundary()), '&&'), ('house', '=')], name='exclude_reservations_overlapping'),
        ),
    ]
