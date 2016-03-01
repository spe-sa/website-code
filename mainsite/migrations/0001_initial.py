# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSpeedZonePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('zid', models.PositiveIntegerField(null=True, verbose_name=b'Zone Id', blank=True)),
                ('aid', models.PositiveIntegerField(null=True, verbose_name=b'Ad Id', blank=True)),
                ('div_id', models.CharField(max_length=100, null=True, verbose_name=b'div id for ad', blank=True)),
                ('div_class', models.CharField(max_length=100, null=True, verbose_name=b'div class for ad', blank=True)),
            ],
            options={
                'ordering': ['zid', 'aid'],
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Tier1Discipline',
            fields=[
                ('number', models.CharField(unique=True, max_length=12)),
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('long_code', models.CharField(max_length=20, null=True, blank=True)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
