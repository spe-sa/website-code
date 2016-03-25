# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_topics'),
        ('spe_blog', '0004_remove_article_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topic'),
        ),
    ]
