# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import taggit.managers
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('spe_blog', '0005_auto_20161115_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(help_text=b'SEO Friendly name that is unique for use in URL', max_length=100)),
                ('teaser', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=500, null=True, blank=True)),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=60000)),
                ('publication_date', models.DateField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False, verbose_name='Publish')),
                ('categories', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
    ]
