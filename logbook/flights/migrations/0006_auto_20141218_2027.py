# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20141218_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_dest_ICAO',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_origin_ICAO',
        ),
    ]
