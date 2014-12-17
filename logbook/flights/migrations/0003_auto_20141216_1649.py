# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20141202_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_dest_ICAO',
            field=models.CharField(max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_origin_ICAO',
            field=models.CharField(max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
    ]
