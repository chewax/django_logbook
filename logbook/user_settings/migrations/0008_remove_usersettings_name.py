# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0007_usersettings_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='name',
        ),
    ]
