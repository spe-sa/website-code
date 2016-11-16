# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselcomponentmodel',
            name='is_tracking',
            field=models.BooleanField(default=True, help_text='optional: toggle click through and impression tracking.', verbose_name='Tracking'),
        ),
    ]
