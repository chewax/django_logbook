# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20141202_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplemodelmixin',
            name='description',
            field=models.TextField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
