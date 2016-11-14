# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mainsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titlebarplugin',
            name='backcol',
            field=mainsite.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color', blank=True),
        ),
        migrations.AddField(
            model_name='titlebarplugin',
            name='textcol',
            field=mainsite.models.ColorField(max_length=10, null=True, verbose_name=b'Text Color', blank=True),
        ),
    ]
