# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0021_eventsbycurrentlocationplugin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-date', 'publication']},
        ),
    ]
