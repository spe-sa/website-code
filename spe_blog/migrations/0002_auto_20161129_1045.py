# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brieflistingplugin',
            name='boxtitle',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Box Title', blank=True),
        ),
        migrations.AddField(
            model_name='briefplugin',
            name='boxtitle',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Box Title', blank=True),
        ),
    ]
