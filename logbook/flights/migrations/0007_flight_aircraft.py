# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircrafts', '0002_auto_20141222_1850'),
        ('flights', '0006_auto_20141218_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(default=1, to='aircrafts.Aircraft'),
            preserve_default=False,
        ),
    ]
