# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_issuesbypublicationplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuesbypublicationplugin',
            name='all_url',
            field=models.URLField(null=True, verbose_name=b'Show All URL', blank=True),
        ),
    ]
