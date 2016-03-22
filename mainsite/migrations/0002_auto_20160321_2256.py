# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tier1discipline',
            name='long_code',
        ),
        migrations.AddField(
            model_name='tier1discipline',
            name='crm_code',
            field=models.CharField(max_length=20, null=True, verbose_name=b'CRM code', blank=True),
        ),
        migrations.AddField(
            model_name='tier1discipline',
            name='eva_code',
            field=models.CharField(max_length=20, null=True, verbose_name=b'EVA code', blank=True),
        ),
    ]
