# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('spe_events', '0001_initial'),
        ('spe_promotions', '0008_auto_20161205_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleeventpromotionlistingplugin',
            name='disciplines',
        ),
        migrations.RemoveField(
            model_name='eventformemberlistingplugin',
            name='use_browsing_location',
        ),
        migrations.AddField(
            model_name='eventpromotionbydisciplinelistingplugin',
            name='event_type',
            field=models.ManyToManyField(to='spe_events.EventType'),
        ),
        migrations.AddField(
            model_name='eventpromotionbyregionlistingplugin',
            name='event_type',
            field=models.ManyToManyField(to='spe_events.EventType'),
        ),
        migrations.AddField(
            model_name='eventpromotionbytopiclistingplugin',
            name='event_type',
            field=models.ManyToManyField(to='spe_events.EventType'),
        ),
        migrations.AlterField(
            model_name='eventformemberlistingplugin',
            name='show',
            field=models.CharField(default=b'discipline', max_length=255, choices=[(b'discipline', b'Events in Discipline Regardless of Region'), (b'region', b'Regional Events Only')]),
        ),
        migrations.AlterField(
            model_name='eventformemberlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionbydisciplinelistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionbyregionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionbytopiclistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.AlterField(
            model_name='eventpromotioninuserregionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionselectionplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.AlterField(
            model_name='promotionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/promotion_posts.html', b'Listing')]),
        ),
        migrations.DeleteModel(
            name='EventPromotionNearLocationListingPlugin',
        ),
        migrations.DeleteModel(
            name='EventPromotionNearUserListingPlugin',
        ),
        migrations.DeleteModel(
            name='SimpleEventPromotionListingPlugin',
        ),
    ]
