# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import spe_blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesplugin',
            name='boxtitle',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Box Title', blank=True),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='backcol',
            field=spe_blog.models.ColorField(default=b'#ffffff', max_length=10, null=True, verbose_name=b'Background Color', blank=True),
        ),
    ]
