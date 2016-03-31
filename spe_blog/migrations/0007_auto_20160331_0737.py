# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0006_auto_20160330_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar')]),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar')]),
        ),
    ]
