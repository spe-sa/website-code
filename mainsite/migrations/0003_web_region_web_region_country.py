# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20161101_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_code', models.CharField(unique=True, max_length=15)),
                ('region_name', models.CharField(unique=True, max_length=50)),
                ('is_visible', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Web_Region_Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_UN', models.CharField(max_length=25, verbose_name=b'Country Code')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='mainsite.Web_Region', null=True)),
            ],
            options={
                'verbose_name': 'Web Region Country',
                'verbose_name_plural': 'Web Region Countries',
            },
        ),
    ]
