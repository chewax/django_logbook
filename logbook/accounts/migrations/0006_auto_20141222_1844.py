# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20141209_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='license_number',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
