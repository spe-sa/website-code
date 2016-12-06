# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_promotions', '0009_auto_20161203_0656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simpleeventnonmembermessage',
            options={'verbose_name': 'Promotion for Non-Member or Member Not Logged In'},
        ),
    ]
