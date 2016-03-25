# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_breadcrumbplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='topics',
        ),
    ]
