# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0011_auto_20150106_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='role',
            field=models.CharField(default=b'PIC', max_length=4, blank=True, choices=[(b'PIC', b'Pilot in command'), (b'SIC', b'Second in command'), (b'INT', b'Instructor'), (b'INP', b'Inspector'), (b'ENG', b'Engineer'), (b'NAV', b'Navigator'), (b'CCR', b'Cabin Crew')]),
            preserve_default=True,
        ),
    ]
