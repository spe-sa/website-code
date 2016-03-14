# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0018_remove_issuesbypublicationplugin_issue_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='subscribe_url',
        ),
    ]
