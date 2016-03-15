# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0005_auto_20160314_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_main', models.CharField(max_length=100, verbose_name=b'Title')),
                ('title_sub', models.CharField(max_length=100, verbose_name=b'Title')),
                ('picture', models.ImageField(upload_to=b'authors', null=True, verbose_name='Picture of Author', blank=True)),
                ('picture_alternate', models.CharField(max_length=50, null=True, verbose_name='Picture alternate text', blank=True)),
                ('picture_caption', models.CharField(max_length=250, null=True, verbose_name='Picture caption', blank=True)),
                ('picture_attribution', models.CharField(max_length=255, null=True, verbose_name='Picture attribution', blank=True)),
                ('author_bio', ckeditor.fields.RichTextField(help_text='Author Bio', max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Editorials',
            },
        ),
        migrations.RemoveField(
            model_name='editorialplugin',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='editorialplugin',
            name='title',
        ),
        migrations.AddField(
            model_name='editorialplugin',
            name='editorial',
            field=models.ManyToManyField(to='spe_blog.Editorial'),
        ),
    ]
