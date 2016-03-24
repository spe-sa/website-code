# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20160323_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default='1', serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topics',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
