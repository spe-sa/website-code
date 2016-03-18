# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_articledetailplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articledetailplugin',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='spe_blog.Article', null=True),
        ),
    ]
