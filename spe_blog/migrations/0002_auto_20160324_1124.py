# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breadcrumbplugin',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='BreadCrumbPlugin',
        ),
    ]
