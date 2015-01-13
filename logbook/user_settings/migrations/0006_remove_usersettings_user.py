# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0005_auto_20150110_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='user',
        ),
    ]
