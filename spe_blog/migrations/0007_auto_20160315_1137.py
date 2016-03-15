# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0006_auto_20160315_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorial',
            name='exerpt',
            field=ckeditor.fields.RichTextField(default='exerpt', help_text='Exerpt', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='editorialplugin',
            name='articles',
            field=models.ManyToManyField(to='spe_blog.Article'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='author_bio',
            field=ckeditor.fields.RichTextField(help_text='Author Bio', max_length=500),
        ),
    ]
