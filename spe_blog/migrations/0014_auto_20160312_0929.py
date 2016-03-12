# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0013_auto_20160312_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuesbypublicationplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/issue_channel.html', max_length=255, choices=[(b'spe_blog/plugins/issue_channel.html', b'Issue channel'), (b'spe_blog/plugins/issue_sidebar.html', b'Issue sidebar')]),
        ),
    ]
