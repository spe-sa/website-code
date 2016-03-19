# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0005_breadcrumbplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breadcrumbplugin',
            name='levels',
        ),
        migrations.AddField(
            model_name='breadcrumbplugin',
            name='title',
            field=models.CharField(default='tt', max_length=50),
            preserve_default=False,
        ),
    ]
