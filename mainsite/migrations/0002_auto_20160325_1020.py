# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='id',
            field=models.PositiveIntegerField(serialize=False, primary_key=True),
        ),
    ]
