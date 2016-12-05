# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('spe_events', '0001_initial'),
        ('spe_promotions', '0007_auto_20161203_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='event_type',
            field=models.ForeignKey(default=1, to='spe_events.EventType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventpromotionnearlocationlistingplugin',
            name='radius',
            field=models.FloatField(verbose_name=b'Radius in km', validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='last_impression',
            field=models.DateTimeField(default=datetime.date(2016, 11, 5), editable=False),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotionlistingplugin',
            name='radius',
            field=models.FloatField(verbose_name=b'Radius in km', validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
    ]
