# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tier1discipline',
            options={'ordering': ['name'], 'verbose_name': 'Discipline'},
        ),
        migrations.AlterModelOptions(
            name='topics',
            options={'ordering': ['name'], 'verbose_name': 'Topic'},
        ),
    ]
