# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_article_freed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='freed',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Publication Date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='free_start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Start Date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='free_stop',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'End Date'),
        ),
    ]
