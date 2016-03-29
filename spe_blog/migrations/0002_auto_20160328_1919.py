# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', null=True, verbose_name=b'Topic', blank=True),
        ),
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='personalized',
            field=models.BooleanField(default=False),
        ),
    ]
