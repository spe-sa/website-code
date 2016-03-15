# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0008_auto_20160315_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuesbypublicationplugin',
            name='subscribe_url',
        ),
    ]
