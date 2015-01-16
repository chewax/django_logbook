# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0010_auto_20150113_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='max_service_3m',
            field=models.IntegerField(default=400, verbose_name=b'Maximum service hours per 3 month'),
            preserve_default=True,
        ),
    ]
