# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_textplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('last_year_paid', models.PositiveIntegerField()),
                ('first_member_date', models.DateField()),
                ('continuous_start_date', models.DateField()),
                ('expected_grad_year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAchievements',
            fields=[
                ('customerclassification_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mainsite.CustomerClassification')),
                ('sort_order', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('weight', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            bases=('mainsite.customerclassification',),
        ),
        migrations.AddField(
            model_name='customer',
            name='classifications',
            field=models.ManyToManyField(related_name='classification_customers', to='mainsite.CustomerClassification', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='primary_discipline',
            field=models.ForeignKey(related_name='primary_customers', blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='secondary_discipline',
            field=models.ForeignKey(related_name='secondary_customers', blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='subscriptions',
            field=models.ManyToManyField(to='mainsite.CustomerSubscription', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='achievements',
            field=models.ManyToManyField(related_name='achievement_customers', to='mainsite.CustomerAchievements', blank=True),
        ),
    ]
