# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0008_auto_20160305_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='expected_grad_year',
            field=models.DateField(),
        ),
    ]
