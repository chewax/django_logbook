# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0003_auto_20141216_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_dest_ICAO',
            field=models.CharField(max_length=4, null=True, verbose_name=b'To', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_origin_ICAO',
            field=models.CharField(max_length=4, null=True, verbose_name=b'From', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='arrival_airport',
            field=models.CharField(max_length=4, verbose_name=b'To:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='departure_airport',
            field=models.CharField(max_length=4, verbose_name=b'From:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='time_in',
            field=models.DateTimeField(verbose_name=b'IN'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='time_off',
            field=models.DateTimeField(verbose_name=b'OFF'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='time_on',
            field=models.DateTimeField(verbose_name=b'ON'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flightleg',
            name='time_out',
            field=models.DateTimeField(verbose_name=b'OUT'),
            preserve_default=True,
        ),
    ]
