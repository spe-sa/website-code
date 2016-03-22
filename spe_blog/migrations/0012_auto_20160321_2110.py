# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text="Introductory paragraph or 'teaser.' for paywal", null=True, blank=True),
        ),
    ]
