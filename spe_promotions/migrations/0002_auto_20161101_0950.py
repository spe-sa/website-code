# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpromotionbydisciplinelistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionnearlocationlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionnearuserlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')]),
        ),
        migrations.AlterField(
            model_name='promotionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')]),
        ),
    ]
