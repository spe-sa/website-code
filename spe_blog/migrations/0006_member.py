# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0005_article_sponsored'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('constit_id', models.PositiveIntegerField()),
                ('primary_discipline', models.CharField(max_length=4)),
                ('secondary_discipline', models.CharField(max_length=4)),
                ('email', models.EmailField(max_length=254)),
                ('JPT_subscription', models.BooleanField()),
                ('TWA_subscription', models.BooleanField()),
                ('OGF_subscription', models.BooleanField()),
                ('HSE_subscription', models.BooleanField()),
                ('membership_type', models.CharField(max_length=30)),
                ('professional', models.BooleanField()),
                ('student', models.BooleanField()),
                ('yp', models.BooleanField()),
                ('lifetime', models.BooleanField()),
                ('paid', models.BooleanField()),
                ('first_member_date', models.DateField()),
                ('current_member_start', models.DateField()),
                ('renewed_next_year', models.BooleanField()),
            ],
        ),
    ]
