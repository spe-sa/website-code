# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_auto_20160328_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Full text of the article.', max_length=35000),
        ),
        migrations.AlterField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topics of Interest', blank=True),
        ),
    ]
