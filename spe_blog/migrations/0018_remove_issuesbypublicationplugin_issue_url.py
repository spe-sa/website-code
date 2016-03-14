# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0017_auto_20160312_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuesbypublicationplugin',
            name='issue_url',
        ),
    ]
