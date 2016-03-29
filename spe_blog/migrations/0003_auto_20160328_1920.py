# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_auto_20160328_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topic', blank=True),
        ),
    ]
