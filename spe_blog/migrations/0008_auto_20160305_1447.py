# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0007_auto_20160304_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='century_club',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='distinguished',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='expected_grad_year',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='honorary',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='key_club',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='legion_of_honor',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
