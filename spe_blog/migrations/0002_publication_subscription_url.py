# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='subscription_url',
            field=models.URLField(null=True, verbose_name='Subscription URL', blank=True),
        ),
    ]
