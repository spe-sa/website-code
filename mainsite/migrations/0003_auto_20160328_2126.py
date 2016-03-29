# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['region_name'],
                'verbose_name': 'Region',
            },
        ),
        migrations.AlterModelOptions(
            name='countries',
            options={'ordering': ['country_name'], 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AddField(
            model_name='countries',
            name='region',
            field=models.ForeignKey(blank=True, to='mainsite.Regions', null=True),
        ),
    ]
