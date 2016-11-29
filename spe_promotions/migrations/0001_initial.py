# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import filer.fields.image
import django.db.models.deletion
import cms.models.fields
import django.core.validators
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('spe_blog', '0001_initial'),
        ('mainsite', '0001_initial'),
        ('filer', '0004_auto_20160328_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPromotionByDisciplineListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('disciplines', models.ManyToManyField(to='mainsite.Tier1Discipline', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
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
        migrations.CreateModel(
            name='EventPromotionNearLocationListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('radius', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventPromotionNearUserListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('radius', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('teaser', ckeditor_uploader.fields.RichTextUploadingField(max_length=300)),
                ('is_logo', models.BooleanField(default=False, verbose_name=b'LOGO')),
                ('picture_alternate', models.CharField(max_length=250, null=True, verbose_name='Picture alternate text', blank=True)),
                ('hits', models.PositiveIntegerField(default=0, editable=False)),
                ('impressions', models.PositiveIntegerField(default=0, editable=False)),
                ('last_impression', models.DateTimeField(default=datetime.date(2016, 10, 30), editable=False)),
                ('promotion_type', models.CharField(default=b'generic', max_length=40, verbose_name=b'Promotion Type', choices=[(b'article', b'Article'), (b'book', b'Book'), (b'event', b'Event'), (b'webinar', b'Webinar'), (b'generic', b'Generic')])),
                ('start', models.DateField(verbose_name=b'Start Date')),
                ('end', models.DateField(verbose_name=b'End Date')),
                ('click_url', models.URLField(null=True, verbose_name='Click Through External URL', blank=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('url', models.URLField(null=True, editable=False, blank=True)),
                ('article', models.ForeignKey(blank=True, to='spe_blog.Article', null=True)),
                ('click_page', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Click Through Page', blank=True, to='cms.Page', null=True)),
                ('disciplines', models.ManyToManyField(to='mainsite.Tier1Discipline', blank=True)),
                ('picture', filer.fields.image.FilerImageField(related_name='promotion_picture', verbose_name='Picture for article', to='filer.Image')),
                ('regions', models.ManyToManyField(to='mainsite.Regions', blank=True)),
            ],
            options={
                'ordering': ['-end', 'title'],
                'get_latest_by': ['end'],
            },
        ),
        migrations.CreateModel(
            name='PromotionListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('promotion_type', models.CharField(default=b'generic', max_length=40, verbose_name=b'Promotion Type', choices=[(b'article', b'Article'), (b'book', b'Book'), (b'event', b'Event'), (b'webinar', b'Webinar'), (b'generic', b'Generic')])),
                ('disciplines', models.ManyToManyField(to='mainsite.Tier1Discipline', blank=True)),
                ('regions', models.ManyToManyField(to='mainsite.Regions', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SimpleEventPromotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=250)),
                ('event_date', models.DateField(verbose_name=b'Event Date')),
                ('event_location', models.CharField(max_length=50)),
                ('teaser', ckeditor_uploader.fields.RichTextUploadingField(max_length=300)),
                ('hits', models.PositiveIntegerField(default=0, editable=False)),
                ('impressions', models.PositiveIntegerField(default=0, editable=False)),
                ('last_impression', models.DateTimeField(default=datetime.date(2016, 10, 30), editable=False)),
                ('latitude', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('start', models.DateField(verbose_name=b'Display Start Date')),
                ('end', models.DateField(verbose_name=b'Display End Date')),
                ('sponsored', models.BooleanField(default=False)),
                ('click_url', models.URLField(null=True, verbose_name='Click Through External URL', blank=True)),
                ('url', models.URLField(null=True, editable=False, blank=True)),
                ('disciplines', models.ManyToManyField(to='mainsite.Tier1Discipline', blank=True)),
                ('picture', filer.fields.image.FilerImageField(related_name='simple_promotion_picture', verbose_name='Picture for event promotion', to='filer.Image')),
                ('regions', models.ManyToManyField(to='mainsite.Web_Region', blank=True)),
                ('topics', models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True)),
            ],
            options={
                'ordering': ['-end', 'event'],
                'get_latest_by': ['end'],
            },
        ),
        migrations.CreateModel(
            name='SimpleEventPromotionListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay'), (b'spe_promotions/plugins/jb_carousel.html', b'JB Carousel')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('radius', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('disciplines', models.ManyToManyField(to='mainsite.Tier1Discipline', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
