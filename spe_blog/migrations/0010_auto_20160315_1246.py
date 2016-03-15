# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0009_remove_issuesbypublicationplugin_subscribe_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editorialplugin',
            old_name='link',
            new_name='lnk',
        ),
    ]
