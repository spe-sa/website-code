# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0019_auto_20160316_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='free_stop',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name=b'End Date', blank=True),
        ),
    ]
