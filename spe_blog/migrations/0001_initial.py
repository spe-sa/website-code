# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ckeditor.fields
import django.utils.timezone
import cms.models.fields
import taggit.managers
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cms', '0013_urlconfrevision'),
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('sponsored', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=False, verbose_name='Always Free')),
                ('free_start', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('free_stop', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(help_text=b'SEO Friendly name that is unique for use in URL', max_length=100)),
                ('teaser', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250, null=True, blank=True)),
                ('introduction', ckeditor_uploader.fields.RichTextUploadingField(help_text="Introductory paragraph or 'teaser.' for paywal", null=True, blank=True)),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=35000)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Publication Date')),
                ('picture', models.ImageField(upload_to=b'regular_images', null=True, verbose_name='Picture for article', blank=True)),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('picture_caption', models.CharField(max_length=250, null=True, verbose_name='Picture caption', blank=True)),
                ('picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True)),
                ('author_name', models.CharField(max_length=250, null=True, blank=True)),
                ('author_picture', models.ImageField(upload_to=b'authors', null=True, verbose_name='Picture of Author', blank=True)),
                ('author_picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('author_bio', ckeditor.fields.RichTextField(help_text='Author Bio', max_length=500, null=True, blank=True)),
                ('article_hits', models.PositiveIntegerField(default=0, editable=False)),
                ('article_last_viewed', models.DateTimeField(null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['-date', 'title'],
                'get_latest_by': ['date'],
                'verbose_name': 'article',
            },
        ),
        migrations.CreateModel(
            name='ArticleDetailPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('allow_url_to_override_selection', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='spe_blog.Article', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ArticlesListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Articles')),
                ('order_by', models.CharField(default=b'-article_hits', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('personalized', models.BooleanField(default=False)),
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
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar')])),
                ('order_by', models.CharField(default=b'-article_hits', max_length=20, verbose_name=b'Otherwise order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
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
            name='BreadCrumbPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=50)),
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
            name='Coverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Coverage')),
            ],
            options={
                'verbose_name_plural': 'Coverage',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_main', models.CharField(max_length=100, verbose_name=b'Main Title')),
                ('title_sub', models.CharField(max_length=100, verbose_name=b'Sub-Title')),
                ('exerpt', ckeditor.fields.RichTextField(help_text='Exerpt', max_length=300)),
                ('picture', models.ImageField(upload_to=b'authors', null=True, verbose_name='Picture of Author', blank=True)),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('picture_caption', models.CharField(max_length=250, null=True, verbose_name='Picture caption', blank=True)),
                ('picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True)),
                ('author_bio', ckeditor.fields.RichTextField(help_text='Author Bio', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Editorials',
            },
        ),
        migrations.CreateModel(
            name='EditorialPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/editorial.html', max_length=255, choices=[(b'spe_blog/plugins/editorial.html', b'Editorial')])),
                ('lnk', models.URLField(null=True, verbose_name=b'Link URL', blank=True)),
                ('editorial', models.ManyToManyField(to='spe_blog.Editorial')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
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
            options={
                'ordering': ['-date', 'publication'],
            },
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
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='IssuesByYearPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
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
                ('subscription_url', models.URLField(null=True, verbose_name='Subscription URL', blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='issuesbyyearplugin',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication'),
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
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='spe_blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='coverage',
            field=models.ManyToManyField(to='spe_blog.Coverage', blank=True),
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
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('publication', 'print_volume', 'print_issue', 'slug', 'date')]),
        ),
    ]
