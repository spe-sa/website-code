# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('spe_links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spelink',
            name='url',
        ),
        migrations.RemoveField(
            model_name='spelinkcategory',
            name='url',
        ),
        migrations.AddField(
            model_name='spelink',
            name='external_url',
            field=models.URLField(help_text='e.g. http://example.com/thank-you', verbose_name='External URL', blank=True),
        ),
        migrations.AddField(
            model_name='spelink',
            name='page_url',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='A page has priority over an external URL', null=True, verbose_name='Page URL'),
        ),
        migrations.AddField(
            model_name='spelinkcategory',
            name='show_all_external',
            field=models.URLField(help_text='e.g. http://example.com/thank-you', verbose_name='Show all - External URL', blank=True),
        ),
        migrations.AddField(
            model_name='spelinkcategory',
            name='show_all_page',
            field=cms.models.fields.PageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='A page has priority over an external URL', null=True, verbose_name='Show all - Page URL'),
        ),
    ]
