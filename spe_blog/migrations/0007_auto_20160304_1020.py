# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0006_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='current_member_start',
            new_name='continuous_start_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='member',
            name='renewed_next_year',
        ),
        migrations.AddField(
            model_name='member',
            name='currently_board_member',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='currently_committee',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='currently_section_officer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='grad_student',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='last_year_paid',
            field=models.PositiveIntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(default='Ingemar from Ikea', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='new_grad_y1',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='new_grad_y2',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
