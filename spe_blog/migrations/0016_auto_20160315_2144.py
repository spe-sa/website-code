# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0015_articlesplugin_keep_original_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesplugin',
            name='order_by',
            field=models.CharField(default=b'-article_hits', max_length=20, verbose_name=b'Otherwise order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')]),
        ),
    ]
