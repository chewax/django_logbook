# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150110_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='settings',
            field=models.ForeignKey(to='user_settings.UserSettings', null=True),
            preserve_default=True,
        ),
    ]
