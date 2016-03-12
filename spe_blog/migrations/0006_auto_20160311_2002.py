# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0005_auto_20160311_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(null=True, verbose_name=b'Publication Date', blank=True),
        ),
    ]
