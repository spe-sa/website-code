# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0009_auto_20160305_1448'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]
