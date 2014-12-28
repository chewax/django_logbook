# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_flight_aircraft'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightleg',
            name='landings',
            field=models.IntegerField(default=1, verbose_name=b'Landings:'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flightleg',
            name='take_offs',
            field=models.IntegerField(default=1, verbose_name=b'Takeoffs:'),
            preserve_default=True,
        ),
    ]
