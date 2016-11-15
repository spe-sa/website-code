# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20161115_1003'),
        ('spe_blog', '0003_auto_20161115_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='brief',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='mainsite.Web_Region', null=True),
        ),
        migrations.AddField(
            model_name='brieflistingplugin',
            name='regions',
            field=models.ManyToManyField(to='mainsite.Web_Region', blank=True),
        ),
    ]
