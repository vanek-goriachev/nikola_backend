from django.contrib.postgres.operations import BtreeGistExtension
from django.db import migrations


class Migration(migrations.Migration):

    run_before = [
        ('house_reservations', '0001_initial'),
    ]

    operations = [
        BtreeGistExtension(),
    ]
