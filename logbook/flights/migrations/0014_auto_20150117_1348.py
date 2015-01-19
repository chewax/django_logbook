# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0013_flight_crew_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='crew_list',
            field=models.ManyToManyField(to='crews.CrewMember', null=True, verbose_name=b'Crew', blank=True),
            preserve_default=True,
        ),
    ]
