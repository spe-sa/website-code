# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_bio',
            field=ckeditor.fields.RichTextField(help_text='Author Bio', max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_picture',
            field=models.ImageField(upload_to=b'authors', null=True, verbose_name='Picture of Author', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author_picture_alternate',
            field=models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True),
        ),
    ]
