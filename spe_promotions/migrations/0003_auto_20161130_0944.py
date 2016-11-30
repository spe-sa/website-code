# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('spe_promotions', '0002_auto_20161129_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPromotionInUserRegionListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventPromotionSelectionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='article',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='click_page',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='disciplines',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='regions',
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='last_impression',
            field=models.DateTimeField(default=datetime.date(2016, 10, 31), editable=False),
        ),
        migrations.DeleteModel(
            name='Promotion',
        ),
        migrations.AddField(
            model_name='eventpromotionselectionplugin',
            name='promotions',
            field=models.ManyToManyField(to='spe_promotions.SimpleEventPromotion'),
        ),
    ]
