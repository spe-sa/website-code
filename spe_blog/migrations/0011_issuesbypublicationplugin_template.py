# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0010_auto_20160312_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuesbypublicationplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/issue_channel.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Issue channel'), (b'spe_blog/plugins/issue_sidebar.html', b'Issue sidebar')]),
        ),
    ]
