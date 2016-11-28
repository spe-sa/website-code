# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0007_auto_20161128_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleslistingplugin',
            name='boxtitle',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Box Title', blank=True),
        ),
    ]
