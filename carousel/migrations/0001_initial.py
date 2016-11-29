# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselComponentModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('start_display', models.DateField(default=django.utils.timezone.now, null=True, blank=True)),
                ('stop_display', models.DateField(null=True, blank=True)),
                ('link_to', models.URLField(help_text='optional: link to page when carousel item is clicked.', max_length=128, null=True, blank=True)),
                ('is_tracking', models.BooleanField(default=True, help_text='optional: toggle click through and impression tracking.', verbose_name='Tracking')),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('impressions', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CarouselModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', help_text='Optionally set a label for this carousel.', max_length=128, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
