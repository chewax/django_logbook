# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircrafts', '0002_auto_20141222_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='markings',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircrafttype',
            name='original_release',
            field=models.CharField(max_length=15, verbose_name=b'Model'),
            preserve_default=True,
        ),
    ]
