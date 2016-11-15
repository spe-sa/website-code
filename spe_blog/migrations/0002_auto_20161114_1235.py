# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box'), (b'spe_blog/plugins/tech_focus_main.html', b'Tech Focus Main'), (b'spe_blog/plugins/tech_focus_related.html', b'Tech Focus Related')]),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box'), (b'spe_blog/plugins/tech_focus_main.html', b'Tech Focus Main'), (b'spe_blog/plugins/tech_focus_related.html', b'Tech Focus Related')]),
        ),
        migrations.AlterField(
            model_name='tagsdetailplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box'), (b'spe_blog/plugins/tech_focus_main.html', b'Tech Focus Main'), (b'spe_blog/plugins/tech_focus_related.html', b'Tech Focus Related')]),
        ),
        migrations.AlterField(
            model_name='topicsplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box'), (b'spe_blog/plugins/tech_focus_main.html', b'Tech Focus Main'), (b'spe_blog/plugins/tech_focus_related.html', b'Tech Focus Related')]),
        ),
    ]
