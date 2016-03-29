# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_auto_20160328_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Coverage')),
            ],
            options={
                'verbose_name_plural': 'Coverage',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='coverage',
            field=models.ManyToManyField(to='spe_blog.Coverage', blank=True),
        ),
    ]
