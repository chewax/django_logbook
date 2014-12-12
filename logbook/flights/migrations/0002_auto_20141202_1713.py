# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightLeg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departure_airport', models.CharField(max_length=4)),
                ('arrival_airport', models.CharField(max_length=4)),
                ('time_out', models.DateTimeField(verbose_name=b'Time OUT')),
                ('time_off', models.DateTimeField(verbose_name=b'Time OFF')),
                ('time_on', models.DateTimeField(verbose_name=b'Time ON')),
                ('time_in', models.DateTimeField(verbose_name=b'Time IN')),
                ('flight', models.ForeignKey(to='flights.Flight')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='flightlegs',
            name='flight',
        ),
        migrations.DeleteModel(
            name='FlightLegs',
        ),
    ]
