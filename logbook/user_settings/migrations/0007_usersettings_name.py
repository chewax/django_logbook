# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0006_remove_usersettings_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='name',
            field=models.CharField(max_length=40, null=True),
            preserve_default=True,
        ),
    ]
