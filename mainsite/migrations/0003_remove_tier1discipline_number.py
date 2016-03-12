# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20160311_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tier1discipline',
            name='number',
        ),
    ]
