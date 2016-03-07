# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='free_start',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 3, 28, 23, 350720, tzinfo=utc), verbose_name=b'from_date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='free_stop',
            field=models.DateField(default=datetime.datetime(2016, 3, 4, 3, 28, 30, 950494, tzinfo=utc), verbose_name=b'to_date', auto_now_add=True),
            preserve_default=False,
        ),
    ]
