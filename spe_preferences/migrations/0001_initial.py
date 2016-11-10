# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_id', models.CharField(max_length=25)),
                ('customer_id', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('status', models.CharField(default=b'ACTIVE', max_length=12, blank=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('status', models.CharField(default=b'ACTIVE', max_length=12, blank=True)),
                ('sort_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='preference',
            name='group',
            field=models.ForeignKey(to='spe_preferences.PreferenceGroup', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='customerpreference',
            name='preference',
            field=models.ForeignKey(to='spe_preferences.Preference', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
