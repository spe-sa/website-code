# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('mainsite', '0001_initial'),
        ('spe_blog', '0003_auto_20160331_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='BriefDetailPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('allow_url_to_override_selection', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='spe_blog.Brief', on_delete=django.db.models.deletion.PROTECT)),
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
                ('template', models.CharField(default=b'spe_blog/plugins/brief_interest.html', max_length=255, choices=[(b'spe_blog/plugins/issue_channel.html', b'Brief of interest listing'), (b'spe_blog/plugins/brief_index.html', b'Index listing')])),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Briefs')),
                ('order_by', models.CharField(default=b'-article_hits', max_length=20, choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('personalized', models.BooleanField(default=False)),
                ('all_url', models.URLField(null=True, verbose_name=b'Show All URL', blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('category', models.ForeignKey(blank=True, to='spe_blog.Category', null=True)),
                ('publication', models.ForeignKey(blank=True, to='spe_blog.Publication', null=True)),
                ('topic', models.ForeignKey(blank=True, to='mainsite.Topics', null=True)),
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
                ('template', models.CharField(default=b'spe_blog/plugins/brief_interest.html', max_length=255, choices=[(b'spe_blog/plugins/issue_channel.html', b'Brief of interest listing'), (b'spe_blog/plugins/brief_index.html', b'Index listing')])),
                ('order_by', models.CharField(default=b'-article_hits', max_length=20, verbose_name=b'Otherwise order by', choices=[(b'-article_hits', b'Most Read'), (b'-date', b'Most Recent')])),
                ('all_url', models.CharField(max_length=250, null=True, verbose_name=b'Show All URL', blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('brief', models.ManyToManyField(to='spe_blog.Brief')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
