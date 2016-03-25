# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_remove_article_topics'),
        ('mainsite', '0002_auto_20160325_1020'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topics',
        ),
    ]
