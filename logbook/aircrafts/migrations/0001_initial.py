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
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_number', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factory', models.CharField(max_length=50, verbose_name=b'Manufacturer')),
                ('original_release', models.CharField(max_length=10, verbose_name=b'Model')),
                ('update_number', models.CharField(max_length=10, null=True, verbose_name=b'Version', blank=True)),
                ('short_name', models.CharField(max_length=4, verbose_name=b'Short')),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='model',
            field=models.ForeignKey(to='aircrafts.AircraftType', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
