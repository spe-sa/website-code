# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('mainsite', '0001_initial'),
        ('spe_promotions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPromotionByRegionListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('regions', models.ManyToManyField(to='mainsite.Web_Region', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
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
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 29, 19, 10, 2, 158594, tzinfo=utc), verbose_name=b'Event Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='event_location',
            field=models.CharField(default='blah', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='regions',
            field=models.ManyToManyField(to='mainsite.Web_Region', blank=True),
        ),
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='end',
            field=models.DateField(verbose_name=b'Display End Date'),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='latitude',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='longitude',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='start',
            field=models.DateField(verbose_name=b'Display Start Date'),
        ),
    ]
