# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('spe_blog', '0002_publication_subscription_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorialPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'spe_blog/plugins/editorial.html', max_length=255, choices=[(b'spe_blog/plugins/issue_channel.html', b'Editorial')])),
                ('title', models.CharField(max_length=100)),
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
    ]
