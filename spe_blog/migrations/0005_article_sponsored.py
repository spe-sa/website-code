# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_auto_20160303_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
    ]
