# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spe_promotions', '0006_auto_20161114_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='last_impression',
            field=models.DateTimeField(default=datetime.date(2016, 10, 16), editable=False),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='last_impression',
            field=models.DateTimeField(default=datetime.date(2016, 10, 16), editable=False),
        ),
    ]
