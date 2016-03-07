# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_auto_20160303_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='freed',
            field=models.BooleanField(default=False),
        ),
    ]
