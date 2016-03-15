# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_editorialplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editorialplugin',
            name='all_text',
        ),
        migrations.RemoveField(
            model_name='editorialplugin',
            name='all_url',
        ),
        migrations.RemoveField(
            model_name='editorialplugin',
            name='order_by',
        ),
    ]