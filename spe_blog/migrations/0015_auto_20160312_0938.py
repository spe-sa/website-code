# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0014_auto_20160312_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuesbypublicationplugin',
            name='issue_url',
            field=models.URLField(null=True, verbose_name=b'Show All URL', blank=True),
        ),
        migrations.AddField(
            model_name='issuesbypublicationplugin',
            name='subscribe_url',
            field=models.URLField(null=True, verbose_name=b'Show All URL', blank=True),
        ),
    ]
