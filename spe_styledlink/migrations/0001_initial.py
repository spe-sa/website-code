# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyledLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default=b'', help_text='Required. The text that is linked.', max_length=255, verbose_name='link text', blank=True)),
                ('title', models.CharField(default=b'', help_text='Optional. If provided, will provide a tooltip for the link.', max_length=255, verbose_name='title', blank=True)),
                ('int_destination_id', models.PositiveIntegerField(null=True, blank=True)),
                ('page_destination', models.CharField(help_text='Use this to specify an intra-page link. Can be used for the <em>current page</em> or with a specific internal destination. Do <strong>not</strong> include a leading \u201c#\u201d.', max_length=64, verbose_name='intra-page destination', blank=True)),
                ('int_hash', models.BooleanField(default=False)),
                ('ext_destination', models.TextField(default=b'', verbose_name='external destination', blank=True)),
                ('ext_follow', models.BooleanField(default=True, help_text='Let search engines follow this hyperlink?', verbose_name='follow external link?')),
                ('mailto', models.EmailField(help_text='An email address. This will override an external url.', max_length=254, null=True, verbose_name='email address', blank=True)),
                ('target', models.CharField(default=b'', choices=[(b'', 'same window'), (b'_blank', 'new window'), (b'_parent', 'parent window'), (b'_top', 'topmost frame')], max_length=100, blank=True, help_text='Optional. Specify if this link should open in a new tab or window.', verbose_name='target')),
                ('int_destination_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='StyledLinkStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(default=b'', help_text='The internal name of this link style.', max_length=32, verbose_name='label')),
                ('link_class', models.CharField(default=b'', help_text=b'The class to add to this link (do NOT preceed with a ".").', max_length=32, verbose_name='link class')),
            ],
        ),
        migrations.AddField(
            model_name='styledlink',
            name='styles',
            field=models.ManyToManyField(related_name='styled_link_style', default=None, to='spe_styledlink.StyledLinkStyle', blank=True, help_text='Optional. Choose one or more styles for this link.', null=True, verbose_name='link style'),
        ),
    ]
