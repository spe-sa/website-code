# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('magazine', models.CharField(default=b'JPT', max_length=4, verbose_name=b'Magazine', choices=[(b'JPT', b'Journal of Petroleum Technology'), (b'TWA', b'The Way Ahead'), (b'OGF', b'Oil and Gas Facilities'), (b'HSE', b'HSE Now'), (b'WWW', b'Online')])),
                ('issue', models.PositiveIntegerField(default=1)),
                ('article_number', models.PositiveIntegerField(default=1)),
                ('title', models.CharField(max_length=250)),
                ('subheading', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('introduction', models.TextField(help_text="Introductory paragraph or 'teaser.'")),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=18000)),
                ('date', models.DateField()),
                ('discipline', models.CharField(max_length=4, choices=[(b'D&C', b'Drilling and Completions'), (b'HSE', b'Health, Safety, Security, Environment & Social Responsibility'), (b'M&I', b'Management & Information'), (b'P&O', b'Production & Operations'), (b'PFC', b'Projects, Facilities & Construciton'), (b'RDD', b'Reservoir Description & Dynamics'), (b'UND', b'Undeclared')])),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text.', blank=True)),
                ('picture', models.ImageField(upload_to=b'regular_images', verbose_name='Picture for article')),
                ('picture_caption', models.CharField(max_length=250, null=True, verbose_name='Picture caption', blank=True)),
                ('article_hits', models.PositiveIntegerField(default=0, editable=False)),
                ('article_last_viewed', models.DateTimeField(null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleByPublicationPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=50)),
                ('magazine', models.CharField(default=b'JPT', max_length=4, verbose_name=b'Magazine', choices=[(b'JPT', b'Journal of Petroleum Technology'), (b'TWA', b'The Way Ahead'), (b'OGF', b'Oil and Gas Facilities'), (b'HSE', b'HSE Now'), (b'WWW', b'Online')])),
                ('articles', models.PositiveIntegerField(default=5)),
                ('orderby', models.CharField(default=b'-article_hits', max_length=20, verbose_name=b'Order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=0, verbose_name='Starting With')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ArticleDisciplineByUserPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=50)),
                ('articles', models.PositiveIntegerField(default=5)),
                ('orderby', models.CharField(default=b'-article_hits', max_length=20, verbose_name=b'Order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=0, verbose_name='Starting With')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ArticleDisciplinePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=50)),
                ('discipline', models.CharField(max_length=4, choices=[(b'D&C', b'Drilling and Completions'), (b'HSE', b'Health, Safety, Security, Environment & Social Responsibility'), (b'M&I', b'Management & Information'), (b'P&O', b'Production & Operations'), (b'PFC', b'Projects, Facilities & Construciton'), (b'RDD', b'Reservoir Description & Dynamics'), (b'UND', b'Undeclared')])),
                ('articles', models.PositiveIntegerField(default=5)),
                ('orderby', models.CharField(default=b'-article_hits', max_length=20, verbose_name=b'Order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=0, verbose_name='Starting With')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SelectedFeatureArticlePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(max_length=255, verbose_name=b'Feature type', choices=[(b'spe_blog/image_left_plugin.html', b'Image on left'), (b'spe_blog/featured_plugin.html', b'Image with caption overlay')])),
                ('magazine', models.CharField(default=b'JPT', max_length=4, verbose_name=b'From magazine', choices=[(b'JPT', b'Journal of Petroleum Technology'), (b'TWA', b'The Way Ahead'), (b'OGF', b'Oil and Gas Facilities'), (b'HSE', b'HSE Now'), (b'WWW', b'Online')])),
                ('issue', models.PositiveIntegerField(default=1)),
                ('article_number', models.PositiveIntegerField(default=1, verbose_name='Article number')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('magazine', 'issue', 'article_number')]),
        ),
    ]
