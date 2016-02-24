# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSpeedZoneAdPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=255, verbose_name=b'Advertising Block Name')),
                ('div_id', models.CharField(max_length=100, null=True, verbose_name=b'div id for ad', blank=True)),
                ('div_class', models.CharField(max_length=100, null=True, verbose_name=b'div class for ad', blank=True)),
                ('zid', models.PositiveIntegerField(verbose_name=b'Zone id')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
