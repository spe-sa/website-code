# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_promotions', '0014_eventpromotionbyregionlistingplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='event_location',
            field=models.CharField(default='here', max_length=50),
            preserve_default=False,
        ),
    ]
