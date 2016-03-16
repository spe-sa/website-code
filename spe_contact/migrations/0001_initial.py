# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0010_auto_20160315_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_id', models.CharField(max_length=12, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('publication', models.ForeignKey(to='spe_blog.Publication')),
            ],
        ),
    ]
