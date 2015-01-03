# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0009_auto_20150103_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='duty',
            field=models.CharField(default=b'FLY', max_length=3, blank=True, choices=[(b'FLY', b'Flight Duty'), (b'SIM', b'Simulator Duty'), (b'DDH', b'Dead Head Duty'), (b'SBY', b'On Standby Duty')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='role',
            field=models.CharField(default=b'PIC', max_length=4, blank=True, choices=[(b'PIC', b'Pilot in command'), (b'SIC', b'Second in command'), (b'ENG', b'Engineer'), (b'NAV', b'Navigator'), (b'CCR', b'Cabin Crew')]),
            preserve_default=True,
        ),
    ]
