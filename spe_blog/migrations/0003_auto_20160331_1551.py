# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_marketoformplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketoformplugin',
            name='description',
        ),
        migrations.AddField(
            model_name='marketoformplugin',
            name='instructions',
            field=models.CharField(default='Instructions', max_length=200, verbose_name=b'Instructions for form'),
            preserve_default=False,
        ),
    ]
