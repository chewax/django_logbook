# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=b'EN', max_length=2, choices=[(b'EN', b'English'), (b'ES', b'Spanish')])),
                ('max_on_30', models.IntegerField(default=90, verbose_name=b'Maximum flight hoursin a month')),
                ('max_on_90', models.IntegerField(default=250, verbose_name=b'Maximum flight hours in 90 days')),
                ('max_on_6m', models.IntegerField(default=450, verbose_name=b'Maximum flight hours in 6 months')),
                ('max_on_12m', models.IntegerField(default=900, verbose_name=b'Maximum flight hours in 12 months')),
                ('max_on_1y', models.IntegerField(default=1000, verbose_name=b'Maximum flight hours per year')),
                ('max_service_1m', models.IntegerField(default=150, verbose_name=b'Maximum service hours per month')),
                ('max_service_1y', models.IntegerField(default=150, verbose_name=b'Maximum service hours per year')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
