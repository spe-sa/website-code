# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('taggit', '0002_auto_20150616_2121'),
        ('spe_blog', '0003_auto_20161201_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogListingPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('look_and_feel', models.CharField(default=b'WWW', max_length=25, choices=[(b'WWW', b'Website'), (b'JPT', b'Jounal of Petroleum Technology'), (b'OGF', b'Oil and Gas Facilities'), (b'TWA', b'The Way Ahead'), (b'HSE', b'HSE Now')])),
                ('template', models.CharField(default=b'spe_blog/plugins/blog_posts.html', max_length=255, choices=[(b'spe_blog/plugins/blog_posts.html', b'Default Blog Post')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Blog Posts')),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('tag_filter', models.CharField(help_text=b"Ex: ( Q(tags__name__icontains='jpt') | Q(tags__name__icontains='twa') ) & ~Q(tags__name__icontains='home')", max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BlogPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('look_and_feel', models.CharField(default=b'WWW', max_length=25, choices=[(b'WWW', b'Website'), (b'JPT', b'Jounal of Petroleum Technology'), (b'OGF', b'Oil and Gas Facilities'), (b'TWA', b'The Way Ahead'), (b'HSE', b'HSE Now')])),
                ('template', models.CharField(default=b'spe_blog/plugins/blog_posts.html', max_length=255, choices=[(b'spe_blog/plugins/blog_posts.html', b'Default Blog Post')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publication_date', 'title']},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='categories',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=b"USE LOWER CASE ONLY! Ex: 'name with space', normal1, normal2 normal3", verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='article_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the blog post.', max_length=20000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(help_text=b'SEO Friendly name that is unique for use in URL', unique=True, max_length=250),
        ),
    ]
