# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0015_auto_20160312_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuesbypublicationplugin',
            name='issue_url',
            field=models.URLField(null=True, verbose_name=b'Issue URL', blank=True),
        ),
        migrations.AlterField(
            model_name='issuesbypublicationplugin',
            name='subscribe_url',
            field=models.URLField(null=True, verbose_name=b'Subscribe URL', blank=True),
        ),
    ]
