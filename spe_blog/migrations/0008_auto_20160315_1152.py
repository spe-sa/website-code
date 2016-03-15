# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0007_auto_20160315_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editorialplugin',
            name='articles',
        ),
        migrations.AddField(
            model_name='editorialplugin',
            name='link',
            field=models.URLField(null=True, verbose_name=b'Link URL', blank=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='title_main',
            field=models.CharField(max_length=100, verbose_name=b'Main Title'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='title_sub',
            field=models.CharField(max_length=100, verbose_name=b'Sub-Title'),
        ),
    ]
