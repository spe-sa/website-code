# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('url', models.URLField(max_length=255, null=True, blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'ordering': ['category__title', 'title'],
                'verbose_name': 'link',
            },
        ),
        migrations.CreateModel(
            name='SpeLinkCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('class_name', models.CharField(max_length=255, null=True, blank=True)),
                ('url', models.URLField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'category',
            },
        ),
        migrations.AddField(
            model_name='spelink',
            name='category',
            field=models.ForeignKey(to='spe_links.SpeLinkCategory', null=True),
        ),
    ]
