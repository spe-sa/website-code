# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_auto_20160404_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='briefplugin',
            old_name='brief',
            new_name='briefs',
        ),
    ]
