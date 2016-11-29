# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20161115_1003'),
        ('spe_promotions', '0011_auto_20161128_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True),
        ),
    ]
