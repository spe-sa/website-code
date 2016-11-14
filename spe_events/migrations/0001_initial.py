# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsByCurrentIPPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('number', models.PositiveIntegerField(default=1)),
                ('radius', models.PositiveIntegerField(default=500, verbose_name=b'Radius around location in km')),
                ('disciplines', models.ManyToManyField(to='mainsite.Tier1Discipline')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='eventsbycurrentipplugin',
            name='types',
            field=models.ManyToManyField(to='spe_events.EventType'),
        ),
    ]
