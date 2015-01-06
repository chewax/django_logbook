# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_auto_20150103_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='duty',
            field=models.CharField(default=b'FLY', max_length=3, blank=True, choices=[(b'FLY', b'Fly'), (b'SIM', b'Simulator'), (b'DDH', b'Dead Head'), (b'SBY', b'Standby')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='rules',
            field=models.CharField(default=b'IFR', max_length=4, blank=True, choices=[(b'IFR', b'IFR'), (b'VFR', b'VFR'), (b'SIFR', b'Simulated IFR')]),
            preserve_default=True,
        ),
    ]
