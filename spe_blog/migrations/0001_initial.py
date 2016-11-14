# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.utils.timezone
import ckeditor.fields
import django.db.models.deletion
import cms.models.fields
import spe_blog.models
import taggit.managers
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('taggit', '0002_auto_20150616_2121'),
        ('mainsite', '0001_initial'),
        ('filer', '0004_auto_20160328_1434'),
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
                ('teaser', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=500, null=True, blank=True)),
                ('introduction', ckeditor_uploader.fields.RichTextUploadingField(help_text="Introductory paragraph or 'teaser.' for paywal", null=True, blank=True)),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=60000)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Publication Date')),
                ('picture_alternate', models.CharField(max_length=250, null=True, verbose_name='Picture alternate text', blank=True)),
                ('picture_caption', models.CharField(max_length=1000, null=True, verbose_name='Picture caption', blank=True)),
                ('picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True)),
                ('article_hits', models.PositiveIntegerField(default=0, editable=False)),
                ('article_last_viewed', models.DateTimeField(null=True, editable=False, blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='Publish')),
                ('editorial_title', models.CharField(max_length=100, null=True, blank=True)),
                ('author_picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Author Picture Attribution', blank=True)),
                ('author_bio', ckeditor.fields.RichTextField(help_text='Author Bio', max_length=500, null=True, blank=True)),
                ('author_picture', filer.fields.image.FilerImageField(related_name='editorial_author_picture', verbose_name='Picture for author', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'ordering': ['-date', 'title'],
                'get_latest_by': ['date'],
                'verbose_name': 'article',
            },
        ),
        migrations.CreateModel(
            name='Article_Tagged',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='spe_blog.Article')),
                ('tag', models.ForeignKey(related_name='spe_blog_article_tagged_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article_TaggedAuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='spe_blog.Article')),
                ('tag', models.ForeignKey(related_name='spe_blog_article_taggedauto_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleDetailPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for article detail page', blank=True, to='cms.Page', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleDetailPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('allow_url_to_override_selection', models.BooleanField(default=False)),
                ('show_related_articles', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Selected article (default)', to='spe_blog.Article')),
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
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Articles')),
                ('order_by', models.CharField(default=b'-date', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('personalized', models.BooleanField(default=False)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('backcol', spe_blog.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color (.for editorials only.)', blank=True)),
                ('fixedheight', models.BooleanField(default=True, verbose_name=b'Fixed Height')),
                ('whitetext', models.BooleanField(default=True, verbose_name=b'White Text')),
                ('boxwidth', models.CharField(default=b'col-md-4', max_length=10, verbose_name=b'TWA Article Box Width', choices=[(b'col-md-12', b'1 Full Width Column'), (b'col-md-6', b'2 Column Format'), (b'col-md-4', b'3 Column Format'), (b'col-md-3', b'4 Column Format')])),
                ('boxheight', models.PositiveIntegerField(default=300, verbose_name=b'TWA Article Box Height', choices=[(300, b'Short Box'), (400, b'Medium Box'), (500, b'Tall Box')])),
                ('all_url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for article listing page', blank=True, to='cms.Page', null=True)),
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
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box')])),
                ('order_by', models.CharField(default=b'-date', max_length=20, verbose_name=b'Otherwise order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('backcol', spe_blog.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color (for editorials only)', blank=True)),
                ('fixedheight', models.BooleanField(default=True, verbose_name=b'Fixed Height')),
                ('whitetext', models.BooleanField(default=True, verbose_name=b'White Text')),
                ('boxwidth', models.CharField(default=b'col-md-4', max_length=10, verbose_name=b'TWA Article Box Width', choices=[(b'col-md-12', b'1 Full Width Column'), (b'col-md-6', b'2 Column Format'), (b'col-md-4', b'3 Column Format'), (b'col-md-3', b'4 Column Format')])),
                ('boxheight', models.PositiveIntegerField(default=300, verbose_name=b'TWA Article Box Height', choices=[(300, b'Short Box'), (400, b'Medium Box'), (500, b'Tall Box')])),
                ('all_url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for article listing page', blank=True, to='cms.Page', null=True)),
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
            name='Brief',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('free', models.BooleanField(default=True, verbose_name='Always Free')),
                ('free_start', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('free_stop', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(help_text=b'SEO Friendly name that is unique for use in URL', max_length=100)),
                ('author', models.CharField(max_length=500, null=True, blank=True)),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=50000)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Publication Date')),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('article_hits', models.PositiveIntegerField(default=0, editable=False)),
                ('article_last_viewed', models.DateTimeField(null=True, editable=False, blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='Publish')),
            ],
            options={
                'ordering': ['-date', 'title'],
                'get_latest_by': ['date'],
                'verbose_name': 'brief',
            },
        ),
        migrations.CreateModel(
            name='Brief_Tagged',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='spe_blog.Brief')),
                ('tag', models.ForeignKey(related_name='spe_blog_brief_tagged_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brief_TaggedAuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='spe_blog.Brief')),
                ('tag', models.ForeignKey(related_name='spe_blog_brief_taggedauto_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BriefDetailPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for brief detail page', blank=True, to='cms.Page', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BriefDetailPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('allow_url_to_override_selection', models.BooleanField(default=False)),
                ('brief', models.ForeignKey(to='spe_blog.Brief', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BriefListingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/brief_interest.html', max_length=255, choices=[(b'spe_blog/plugins/brief_index.html', b'Index listing'), (b'spe_blog/plugins/brief_accordion.html', b'POI Accordion Listing'), (b'spe_blog/plugins/side_list.html', b'Brief List'), (b'spe_blog/plugins/best_shot_1.html', b'Best Shot 1 Col'), (b'spe_blog/plugins/best_shot_2.html', b'Best Shot 2 Col'), (b'spe_blog/plugins/best_shot.html', b'Best Shot 3 Col'), (b'spe_blog/plugins/brief_interest.html', b'Brief of interest listing')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Briefs')),
                ('order_by', models.CharField(default=b'-date', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('backcol', spe_blog.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color', blank=True)),
                ('whitetext', models.BooleanField(default=True, verbose_name=b'White Text')),
                ('all_url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for briefs listing page', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BriefPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/brief_interest.html', max_length=255, choices=[(b'spe_blog/plugins/brief_index.html', b'Index listing'), (b'spe_blog/plugins/brief_accordion.html', b'POI Accordion Listing'), (b'spe_blog/plugins/side_list.html', b'Brief List'), (b'spe_blog/plugins/best_shot_1.html', b'Best Shot 1 Col'), (b'spe_blog/plugins/best_shot_2.html', b'Best Shot 2 Col'), (b'spe_blog/plugins/best_shot.html', b'Best Shot 3 Col'), (b'spe_blog/plugins/brief_interest.html', b'Brief of interest listing')])),
                ('order_by', models.CharField(default=b'-date', max_length=20, verbose_name=b'Otherwise order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('backcol', spe_blog.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color', blank=True)),
                ('whitetext', models.BooleanField(default=True, verbose_name=b'White Text')),
                ('all_url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for briefs listing page', blank=True, to='cms.Page', null=True)),
                ('briefs', models.ManyToManyField(to='spe_blog.Brief')),
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
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_main', models.CharField(max_length=100, verbose_name=b'Main Title')),
                ('title_sub', models.CharField(max_length=100, verbose_name=b'Sub-Title')),
                ('exerpt', ckeditor.fields.RichTextField(help_text='Exerpt', max_length=300)),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('picture_caption', models.CharField(max_length=250, null=True, verbose_name='Picture caption', blank=True)),
                ('picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True)),
                ('author_bio', ckeditor.fields.RichTextField(help_text='Author Bio', max_length=500)),
                ('picture', filer.fields.image.FilerImageField(related_name='editorial_picture', verbose_name='Picture for editorial', blank=True, to='filer.Image', null=True)),
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
                ('backcol', spe_blog.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color', blank=True)),
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
                ('coverblurb', models.TextField(max_length=1000, null=True, verbose_name=b'Cover Description', blank=True)),
                ('covercredit', models.CharField(max_length=1000, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('cover', filer.fields.image.FilerImageField(related_name='cover_picture', verbose_name='Cover', blank=True, to='filer.Image', null=True)),
                ('issue_page', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', null=True)),
            ],
            options={
                'ordering': ['-date', 'publication'],
            },
        ),
        migrations.CreateModel(
            name='IssueCoverPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/on_the_cover.html', max_length=255, choices=[(b'spe_blog/plugins/on_the_cover.html', b'On The Cover'), (b'spe_blog/plugins/issue_sidebar_single.html', b'Subscribe & read issue')])),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'More Items Link', blank=True)),
                ('all_url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for Issue Page', blank=True, to='cms.Page', null=True)),
                ('issue', models.ForeignKey(to='spe_blog.Issue', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='IssuesByPublicationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/issue_channel.html', max_length=255, choices=[(b'spe_blog/plugins/issue_channel.html', b'Issues listing'), (b'spe_blog/plugins/issue_sidebar.html', b'Subscribe & read issue'), (b'spe_blog/plugins/on_the_cover.html', b'On The Cover')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Issues')),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('all_url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for issues listing page', blank=True, to='cms.Page', null=True)),
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
                ('article_url', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for article detail page', blank=True, to='spe_blog.ArticleDetailPage', null=True)),
                ('brief_url', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for brief detail page', blank=True, to='spe_blog.BriefDetailPage', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Category (Secondary)')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories (Secondary)',
            },
        ),
        migrations.CreateModel(
            name='TagsDetailPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Articles')),
                ('order_by', models.CharField(default=b'-date', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('publication', models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TagsPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for tags page', blank=True, to='cms.Page', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicsListPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/topics_list_3col.html', max_length=255, choices=[(b'spe_blog/plugins/topics_list_1col.html', b'Topic List 1 Column'), (b'spe_blog/plugins/topics_list.html', b'Topic List 2 Column'), (b'spe_blog/plugins/topics_list_3col.html', b'Topic List 3 Column')])),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='spe_blog.Publication', null=True)),
                ('topics', models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TopicsPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('url', cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for topics page', blank=True, to='cms.Page', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('allow_url_to_override_selection', models.BooleanField(default=False)),
                ('template', models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Image with text below'), (b'spe_blog/plugins/picture_with_text_below_full.html', b'Image with text below full width'), (b'spe_blog/plugins/person_of_interest.html', b'Persons of Interest'), (b'spe_blog/plugins/carousel.html', b'Carousel'), (b'spe_blog/plugins/side_list.html', b'Editorial Sidebar Article List'), (b'spe_blog/plugins/side_feature.html', b'Editorial Sidebar'), (b'spe_blog/plugins/article_editorial.html', b'Editorial w/ Author'), (b'spe_blog/plugins/twa_articlebox.html', b'TWA Article Box'), (b'spe_blog/plugins/twa_featured.html', b'TWA Featured Article Box')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Articles')),
                ('order_by', models.CharField(default=b'-date', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('publication', models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT)),
                ('topics', models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='publication',
            name='tags_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for tags page', blank=True, to='spe_blog.TagsPage', null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='topics_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'URL for topics page', blank=True, to='spe_blog.TopicsPage', null=True),
        ),
        migrations.AddField(
            model_name='issuesbyyearplugin',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='issuesbypublicationplugin',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='issuecoverplugin',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='issue',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='brieflistingplugin',
            name='categories',
            field=models.ManyToManyField(to='spe_blog.Category', blank=True),
        ),
        migrations.AddField(
            model_name='brieflistingplugin',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='spe_blog.Publication', null=True),
        ),
        migrations.AddField(
            model_name='brieflistingplugin',
            name='secondary_categories',
            field=models.ManyToManyField(to='spe_blog.SecondaryCategory', blank=True),
        ),
        migrations.AddField(
            model_name='brieflistingplugin',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Topics', null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='auto_tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.Brief_TaggedAuto', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Auto Tags'),
        ),
        migrations.AddField(
            model_name='brief',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='spe_blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='picture',
            field=filer.fields.image.FilerImageField(related_name='brief_picture', verbose_name='Picture for brief', blank=True, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='brief',
            name='secondary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Category (Secondary)', blank=True, to='spe_blog.SecondaryCategory', null=True),
        ),
        migrations.AddField(
            model_name='brief',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.Brief_Tagged', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Tags'),
        ),
        migrations.AddField(
            model_name='brief',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='categories',
            field=models.ManyToManyField(to='spe_blog.Category', blank=True),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='spe_blog.Publication', null=True),
        ),
        migrations.AddField(
            model_name='articleslistingplugin',
            name='secondary_categories',
            field=models.ManyToManyField(to='spe_blog.SecondaryCategory', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='auto_tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.Article_TaggedAuto', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Auto Tags'),
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
            name='picture',
            field=filer.fields.image.FilerImageField(related_name='article_picture', verbose_name='Picture for article', blank=True, to='filer.Image', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='publication',
            field=models.ForeignKey(to='spe_blog.Publication', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='article',
            name='secondary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Category (Secondary) [TWA ONLY!]', blank=True, to='spe_blog.SecondaryCategory', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.Article_Tagged', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Tags'),
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True),
        ),
        migrations.CreateModel(
            name='ArticleEditor',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'articles (editor view)',
            },
            bases=('spe_blog.article',),
        ),
        migrations.CreateModel(
            name='BriefEditor',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'briefs (editor view)',
            },
            bases=('spe_blog.brief',),
        ),
        migrations.AlterUniqueTogether(
            name='brief',
            unique_together=set([('publication', 'print_volume', 'print_issue', 'slug', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('publication', 'print_volume', 'print_issue', 'slug', 'date')]),
        ),
    ]
