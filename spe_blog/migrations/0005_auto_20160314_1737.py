# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_auto_20160314_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorialplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/editorial.html', max_length=255, choices=[(b'spe_blog/plugins/editorial.html', b'Editorial')]),
        ),
    ]
