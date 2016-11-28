# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0002_carouselcomponentmodel_is_tracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselcomponentmodel',
            name='clicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carouselcomponentmodel',
            name='impressions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
