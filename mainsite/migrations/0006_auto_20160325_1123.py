# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20160325_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tier1discipline',
            name='code',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tier1discipline',
            name='crm_code',
            field=models.CharField(max_length=50, null=True, verbose_name=b'CRM code', blank=True),
        ),
    ]
