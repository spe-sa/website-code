# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Publication Date')),
                ('print_volume', models.PositiveIntegerField(null=True, blank=True)),
                ('print_issue', models.PositiveIntegerField(null=True, blank=True)),
                ('cover', models.ImageField(upload_to=b'covers')),
                ('issue_url', models.URLField()),
                ('subscribe_url', models.URLField()),
                ('active', models.BooleanField(default=True)),
                ('publication', models.ForeignKey(to='spe_blog.Publication')),
            ],
        ),
    ]
