# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsbycurrentipplugin',
            name='disciplines',
            field=models.ManyToManyField(to='mainsite.Tier1Discipline'),
        ),
    ]
