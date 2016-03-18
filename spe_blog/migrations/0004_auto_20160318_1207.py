# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_auto_20160318_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='articledetailplugin',
            name='allow_url_to_override_selection',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='articledetailplugin',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to='spe_blog.Article'),
            preserve_default=False,
        ),
    ]
