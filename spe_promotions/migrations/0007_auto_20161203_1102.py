# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('spe_promotions', '0006_auto_20161202_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventForMemberListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')])),
                ('count', models.PositiveIntegerField(default=5, verbose_name='Number of Promotions')),
                ('show', models.CharField(default=b'discipline', max_length=255, choices=[(b'discipline', b'Events in Discipline Regardless of Region'), (b'region', b'Regional Events Only'), (b'disinreg', b'Events in Discipline in Region Only'), (b'displusreg', b'Events in Discipline Supplemented by Regional Events')])),
                ('use_browsing_location', models.BooleanField(default=True, verbose_name=b'Use Browsing Location if Not Logged In')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SimpleEventMemberMissingDisciplineMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Promotion for Member with No Primary Discipline',
            },
        ),
        migrations.CreateModel(
            name='SimpleEventMemberMissingRegionMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Promotion for Member with No Address',
            },
        ),
        migrations.CreateModel(
            name='SimpleEventNonMemberMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Promotion for Non-Member or Member Not Logged In',
            },
        ),
        migrations.AlterField(
            model_name='eventpromotionbydisciplinelistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionbyregionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionbytopiclistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='eventpromotioninuserregionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionnearlocationlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionnearuserlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='eventpromotionselectionplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='promotionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='last_impression',
            field=models.DateTimeField(default=datetime.date(2016, 11, 3), editable=False),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotionlistingplugin',
            name='template',
            field=models.CharField(default=b'spe_promotions/plugins/carousel.html', max_length=255, choices=[(b'spe_promotions/plugins/carousel.html', b'Carousel'), (b'spe_promotions/plugins/image_left.html', b'Image Left'), (b'spe_promotions/plugins/image_text_below.html', b'Image Top, Text Below'), (b'spe_promotions/plugins/overlay.html', b'Text Overlay')]),
        ),
        migrations.AddField(
            model_name='simpleeventnonmembermessage',
            name='promotion',
            field=models.ForeignKey(verbose_name=b'Promotion for Non-Member or Member Who Has Not Logged In', to='spe_promotions.SimpleEventPromotion'),
        ),
        migrations.AddField(
            model_name='simpleeventmembermissingregionmessage',
            name='promotion',
            field=models.ForeignKey(verbose_name=b'Promotion for Member with no Region', to='spe_promotions.SimpleEventPromotion'),
        ),
        migrations.AddField(
            model_name='simpleeventmembermissingdisciplinemessage',
            name='promotion',
            field=models.ForeignKey(verbose_name=b'Promotion for Member with no Primary Discipline', to='spe_promotions.SimpleEventPromotion'),
        ),
    ]
