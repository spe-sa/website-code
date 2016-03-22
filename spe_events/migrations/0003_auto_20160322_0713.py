# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_events', '0002_auto_20160321_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsbycurrentipplugin',
            name='radius',
            field=models.PositiveIntegerField(default=500, verbose_name=b'Radius around location in km'),
        ),
    ]
