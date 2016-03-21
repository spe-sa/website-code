# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='is_ajax',
            field=models.BooleanField(default=False, help_text='Whether this request was used via javascript.', verbose_name='is ajax'),
        ),
    ]
