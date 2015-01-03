# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0008_auto_20141226_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='duty',
            field=models.CharField(default=b'FLY', max_length=4, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='role',
            field=models.CharField(default=b'PIC', max_length=4, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flightleg',
            name='rules',
            field=models.CharField(default=b'IFR', max_length=4, blank=True),
            preserve_default=True,
        ),
    ]
