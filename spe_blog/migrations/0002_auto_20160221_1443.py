# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedfeaturearticlepluginmodel',
            name='template',
            field=models.CharField(max_length=255, verbose_name=b'Feature type', choices=[(b'spe_blog/image_left_plugin.html', b'Image on left'), (b'spe_blog/featured_overlay.html', b'Image with caption overlay')]),
        ),
    ]
