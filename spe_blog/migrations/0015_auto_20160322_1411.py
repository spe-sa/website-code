# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0014_auto_20160322_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='free',
            field=models.BooleanField(default=False, verbose_name='Always Free'),
        ),
        migrations.AlterField(
            model_name='article',
            name='free_start',
            field=models.DateField(null=True, verbose_name=b'Start Date', blank=True),
        ),
    ]
