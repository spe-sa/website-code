# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_auto_20160311_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='subscribe_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
