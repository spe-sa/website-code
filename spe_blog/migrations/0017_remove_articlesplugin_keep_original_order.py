# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0016_auto_20160315_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesplugin',
            name='keep_original_order',
        ),
    ]
