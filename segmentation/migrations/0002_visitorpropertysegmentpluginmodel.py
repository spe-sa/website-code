# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('segmentation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorPropertySegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('visitor_key', models.CharField(help_text='Name of customer attribute to check.', max_length=500, verbose_name='name of customer attribute')),
                ('visitor_value', models.CharField(help_text='Date format: 2005-12-31 (year-month-day)', max_length=500, verbose_name='value to compare')),
                ('data_type', models.CharField(default='string', max_length=20, verbose_name='Data type to use for comparison', choices=[('string', 'String'), ('date', 'Date'), ('int', 'Int')])),
                ('operator', models.CharField(default='=', max_length=20, verbose_name='Type of comparison', choices=[('=', '='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('!=', '!=')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
