# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_auto_20161201_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpluginmodel',
            name='posts',
            field=models.ManyToManyField(to='spe_blog.Blog'),
        ),
    ]
