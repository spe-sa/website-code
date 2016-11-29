# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('mainsite', '0004_auto_20161115_1003'),
        ('spe_promotions', '0012_simpleeventpromotion_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPromotionByTopicListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('topics', models.ManyToManyField(to='mainsite.Topics', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
