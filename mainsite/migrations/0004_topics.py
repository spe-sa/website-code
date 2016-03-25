# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_delete_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Topic',
            },
        ),
    ]
