# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircrafts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='model',
            field=models.ForeignKey(to='aircrafts.AircraftType'),
            preserve_default=True,
        ),
    ]
