# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_auto_20160328_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Coverage')),
            ],
            options={
                'verbose_name_plural': 'Coverage',
            },
        ),
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
        migrations.AddField(
            model_name='article',
            name='coverage',
            field=models.ManyToManyField(to='spe_blog.Coverage', blank=True),
        ),
    ]
