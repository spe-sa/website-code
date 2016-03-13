# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spelinkcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
