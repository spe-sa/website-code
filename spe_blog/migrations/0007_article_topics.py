# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20160311_1700'),
        ('spe_blog', '0006_auto_20160311_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(to='mainsite.Topics', verbose_name=b'Topic'),
        ),
    ]
