# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('spe_blog', '0015_auto_20160322_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='url',
        ),
        migrations.AddField(
            model_name='publication',
            name='cms_url',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for article detail page', blank=True, to='cms.Page', null=True),
        ),
    ]
