# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_pagetemplate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageTemplate',
        ),
    ]
