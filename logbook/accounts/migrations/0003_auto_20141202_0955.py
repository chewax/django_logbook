# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20141202_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplemodelmixin',
            name='type',
            field=models.CharField(blank=True, max_length=30, choices=[(b'RAT', b'Rating'), (b'TRAT', b'Type Rating'), (b'LIC', b'License')]),
            preserve_default=True,
        ),
    ]
