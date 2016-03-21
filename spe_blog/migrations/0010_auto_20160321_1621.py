# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0009_auto_20160321_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='url',
            field=models.CharField(max_length=255, verbose_name=b'URL for article detail page'),
        ),
    ]
