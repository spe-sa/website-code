# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_web_region_web_region_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='web_region',
            options={'ordering': ['region_name']},
        ),
    ]
