# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0006_remove_usersettings_user'),
        ('accounts', '0006_auto_20141222_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='settings',
            field=models.ForeignKey(to='user_settings.UserSettings', null=True),
            preserve_default=True,
        ),
    ]
