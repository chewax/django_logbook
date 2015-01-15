# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crews', '0002_auto_20150115_1038'),
        ('flights', '0012_auto_20150115_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='crew_list',
            field=models.ManyToManyField(to='crews.CrewMember', null=True, blank=True),
            preserve_default=True,
        ),
    ]
