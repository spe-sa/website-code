# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20161115_1003'),
        ('spe_promotions', '0010_auto_20161128_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 29, 4, 40, 59, 202023, tzinfo=utc), verbose_name=b'Event Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='regions',
            field=models.ManyToManyField(to='mainsite.Web_Region', blank=True),
        ),
        migrations.AddField(
            model_name='simpleeventpromotion',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='end',
            field=models.DateField(verbose_name=b'Display End Date'),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='latitude',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='longitude',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)]),
        ),
        migrations.AlterField(
            model_name='simpleeventpromotion',
            name='start',
            field=models.DateField(verbose_name=b'Display Start Date'),
        ),
    ]
