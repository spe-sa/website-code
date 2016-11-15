# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import spe_blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_auto_20161114_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_title',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='backcol',
            field=spe_blog.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color (for editorials only.)', blank=True),
        ),
    ]
