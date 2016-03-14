# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=False)),
                ('free_start', models.DateField(default=django.utils.timezone.now, verbose_name=b'Start Date')),
                ('free_stop', models.DateField(default=django.utils.timezone.now, verbose_name=b'End Date')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(help_text=b'SEO Friendly name that is unique for use in URL', unique_for_month=b'date', max_length=100)),
                ('teaser', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('introduction', models.TextField(help_text="Introductory paragraph or 'teaser.' for paywal", null=True, blank=True)),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=18000)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Publication Date')),
                ('picture', models.ImageField(upload_to=b'regular_images', null=True, verbose_name='Picture for article', blank=True)),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('picture_caption', models.CharField(max_length=250, null=True, verbose_name='Picture caption', blank=True)),
                ('picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True)),
                ('article_hits', models.PositiveIntegerField(default=0, editable=False)),
                ('article_last_viewed', models.DateTimeField(null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['-date', 'title'],
                'get_latest_by': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ArticlesListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/compact_left_image.html', b'Compact Image on left')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Articles')),
                ('order_by', models.CharField(default=b'-article_hits', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('personalized', models.BooleanField(default=True)),
                ('all_url', models.URLField(null=True, verbose_name=b'Show All URL', blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ArticlesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/compact_left_image.html', b'Compact Image on left')])),
                ('order_by', models.CharField(default=b'-article_hits', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('all_url', models.CharField(max_length=250, null=True, verbose_name=b'Show All URL', blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('articles', models.ManyToManyField(to='spe_blog.Article')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, verbose_name=b'Publication Date', blank=True)),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('cover', models.ImageField(upload_to=b'covers')),
                ('issue_url', models.URLField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssuesByPublicationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/issue_channel.html', max_length=255, choices=[(b'spe_blog/plugins/issue_channel.html', b'Issues listing'), (b'spe_blog/plugins/issue_sidebar.html', b'Subscribe & read issue')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Issues')),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('all_url', models.URLField(null=True, verbose_name=b'Show All URL', blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('subscribe_url', models.URLField(null=True, verbose_name=b'Subscribe URL', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tagged',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='spe_blog.Article')),
                ('tag', models.ForeignKey(related_name='spe_blog_tagged_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedAuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='spe_blog.Article')),
                ('tag', models.ForeignKey(related_name='spe_blog_taggedauto_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='issuesbypublicationplugin',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication'),
        ),
        migrations.AddField(
            model_name='issue',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication'),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='category',
            field=models.ForeignKey(blank=True, to='spe_blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='discipline',
            field=models.ForeignKey(blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='publication',
            field=models.ForeignKey(blank=True, to='spe_blog.Publication', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='auto_tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.TaggedAuto', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Auto Tags'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='spe_blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='disciplines',
            field=models.ManyToManyField(to='mainsite.Tier1Discipline', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.Tagged', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Tags'),
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topic'),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('publication', 'print_volume', 'print_issue', 'slug')]),
        ),
    ]
