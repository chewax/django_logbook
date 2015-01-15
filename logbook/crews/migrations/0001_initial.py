# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(default=b'PIC', max_length=4, blank=True, choices=[(b'PIC', b'Pilot in command'), (b'SIC', b'Second in command'), (b'INT', b'Instructor'), (b'INP', b'Inspector'), (b'ENG', b'Engineer'), (b'NAV', b'Navigator'), (b'CCR', b'Cabin Crew')])),
                ('phone_number', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('company', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
