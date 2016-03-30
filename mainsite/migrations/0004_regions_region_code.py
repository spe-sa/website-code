# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='regions',
            name='region_code',
            field=models.CharField(default='AA', unique=True, max_length=15),
            preserve_default=False,
        ),
    ]
