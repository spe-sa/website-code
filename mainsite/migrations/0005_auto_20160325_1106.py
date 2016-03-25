# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='primary_discipline',
            field=models.ForeignKey(related_name='primary_customers', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='secondary_discipline',
            field=models.ForeignKey(related_name='secondary_customers', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
    ]
