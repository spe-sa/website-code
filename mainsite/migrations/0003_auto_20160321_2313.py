# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20160321_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tier1discipline',
            name='eva_code',
            field=models.CharField(max_length=100, null=True, verbose_name=b'EVA code', blank=True),
        ),
    ]
