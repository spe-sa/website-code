# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('spe_blog', '0002_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuesByPublicationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('cnt', models.PositiveIntegerField(default=5, verbose_name='Number of Articles')),
                ('starting_with', models.PositiveIntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
                ('all_url', models.URLField(max_length=250, null=True, verbose_name=b'Show All URL', blank=True)),
                ('all_text', models.CharField(max_length=50, null=True, verbose_name=b'Show All Text', blank=True)),
                ('publication', models.ForeignKey(to='spe_blog.Publication')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
