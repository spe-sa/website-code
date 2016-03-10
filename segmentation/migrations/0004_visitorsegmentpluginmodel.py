# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('segmentation', '0003_variablesegmentpluginmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('visitor_key', models.CharField(help_text='Name of visitor attribute to check.', max_length=500, verbose_name='name of visitor attribute')),
                ('visitor_value', models.CharField(help_text='Value to consider.', max_length=500, verbose_name='value to compare')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
