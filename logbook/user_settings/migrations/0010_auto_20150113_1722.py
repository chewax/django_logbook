# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0009_usersettings_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='max_on_1m',
            field=models.IntegerField(default=90, verbose_name=b'Maximum flight hours in a month'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='max_on_30',
            field=models.IntegerField(default=90, verbose_name=b'Maximum flight hours in a 30 consecutive days'),
            preserve_default=True,
        ),
    ]
