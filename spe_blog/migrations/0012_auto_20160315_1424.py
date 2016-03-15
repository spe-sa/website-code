# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0011_auto_20160315_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/compact_left_image.html', b'Persons of Interest')]),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/compact_left_image.html', b'Persons of Interest')]),
        ),
    ]
