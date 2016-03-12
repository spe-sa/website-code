# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0007_article_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleslistingplugin',
            name='category',
            field=models.ForeignKey(blank=True, to='spe_blog.Category', null=True),
        ),
    ]
