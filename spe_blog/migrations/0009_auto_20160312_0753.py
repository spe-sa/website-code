# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0008_articleslistingplugin_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Picture with text below')]),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/image_left.html', max_length=255, choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay'), (b'spe_blog/plugins/picture_with_text_below.html', b'Picture with text below')]),
        ),
        migrations.AlterField(
            model_name='issuesbypublicationplugin',
            name='cnt',
            field=models.PositiveIntegerField(default=5, verbose_name='Number of Issues'),
        ),
    ]
