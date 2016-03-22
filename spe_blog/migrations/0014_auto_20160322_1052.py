# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0013_auto_20160322_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='free_stop',
            field=models.DateField(null=True, verbose_name=b'End Date', blank=True),
        ),
    ]
