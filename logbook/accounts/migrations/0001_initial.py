# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleModelMixin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=4)),
                ('type', models.CharField(max_length=30, blank=True)),
                ('description', models.TextField(max_length=300, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('simplemodelmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.SimpleModelMixin')),
            ],
            options={
            },
            bases=('accounts.simplemodelmixin',),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('simplemodelmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='accounts.SimpleModelMixin')),
            ],
            options={
            },
            bases=('accounts.simplemodelmixin',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(unique=True, max_length=50, verbose_name='username')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='email')),
                ('enabled', models.BooleanField(default=True)),
                ('display_real_name', models.BooleanField(default=False)),
                ('preferred_timezone', models.CharField(default=b'Automatic', max_length=32)),
                ('license_number', models.CharField(max_length=15)),
                ('licences', models.ManyToManyField(to='accounts.License', null=True, blank=True)),
                ('ratings', models.ManyToManyField(to='accounts.Rating', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
