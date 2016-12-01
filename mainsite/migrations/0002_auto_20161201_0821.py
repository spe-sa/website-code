# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileimgback',
            name='ttl',
            field=models.CharField(max_length=250, verbose_name=b'Title', blank=True),
        ),
    ]
