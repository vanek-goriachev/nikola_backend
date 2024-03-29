# Generated by Django 5.0.3 on 2024-03-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название события')),
                ('start_date', models.DateField(verbose_name='Дата начала события')),
                ('end_date', models.DateField(verbose_name='Дата конца события')),
                ('multiplier', models.FloatField(default=1, verbose_name='Множитель события')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания события')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения события')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
    ]
