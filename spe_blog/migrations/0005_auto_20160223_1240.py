# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_discipline'),
        ('taggit', '0002_auto_20150616_2121'),
        ('spe_blog', '0004_auto_20160221_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagged',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedAuto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='discipline',
        ),
        migrations.AddField(
            model_name='article',
            name='disciplines',
            field=models.ManyToManyField(to='mainsite.Discipline', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='picture_attribution',
            field=models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture_alternate',
            field=models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True),
        ),
        migrations.AddField(
            model_name='taggedauto',
            name='content_object',
            field=models.ForeignKey(to='spe_blog.Article'),
        ),
        migrations.AddField(
            model_name='taggedauto',
            name='tag',
            field=models.ForeignKey(related_name='spe_blog_taggedauto_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='tagged',
            name='content_object',
            field=models.ForeignKey(to='spe_blog.Article'),
        ),
        migrations.AddField(
            model_name='tagged',
            name='tag',
            field=models.ForeignKey(related_name='spe_blog_tagged_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='auto_tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.TaggedAuto', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Auto Tags'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='spe_blog.Tagged', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Tags'),
        ),
    ]
