# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20150110_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='settings',
            field=models.OneToOneField(related_name='user_settings', null=True, to='user_settings.UserSettings'),
            preserve_default=True,
        ),
    ]
