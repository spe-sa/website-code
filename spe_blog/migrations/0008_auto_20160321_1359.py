# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0007_auto_20160321_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='url',
            field=models.URLField(default='www.spe.org', verbose_name=b'URL for article detail page'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=ckeditor.fields.RichTextField(help_text="Introductory paragraph or 'teaser.' for paywal", null=True, blank=True),
        ),
    ]
