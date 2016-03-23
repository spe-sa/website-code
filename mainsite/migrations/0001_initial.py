# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSpeedZonePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('zid', models.PositiveIntegerField(null=True, verbose_name=b'Zone Id', blank=True)),
                ('aid', models.PositiveIntegerField(null=True, verbose_name=b'Ad Id', blank=True)),
                ('num', models.PositiveIntegerField(null=True, verbose_name=b'Number of Ads', blank=True)),
                ('show_errors', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['zid', 'aid'],
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
                ('prefix', models.CharField(max_length=50, null=True, blank=True)),
                ('suffix', models.CharField(max_length=20, null=True, blank=True)),
                ('first_name', models.CharField(max_length=80, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=60, null=True, blank=True)),
                ('last_name', models.CharField(max_length=60, null=True, blank=True)),
                ('nickname', models.CharField(max_length=80, null=True, blank=True)),
                ('formal_salutation', models.CharField(max_length=180, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('gender', models.CharField(max_length=12, null=True, blank=True)),
                ('address1', models.CharField(max_length=255, null=True, blank=True)),
                ('address2', models.CharField(max_length=255, null=True, blank=True)),
                ('address3', models.CharField(max_length=255, null=True, blank=True)),
                ('address4', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('zip', models.CharField(max_length=100, null=True, blank=True)),
                ('allow_email', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('membership_status', models.CharField(max_length=50, null=True, blank=True)),
                ('paid_through_date', models.DateField(null=True, blank=True)),
                ('original_member_date', models.DateField(null=True, blank=True)),
                ('continuous_member_date', models.DateField(null=True, blank=True)),
                ('expected_grad_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerClassification',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('type', models.CharField(default=b'MEMBERSHIP', max_length=20, null=True, blank=True, choices=[(b'MEMBERSHIP', b'Membership'), (b'ACHIEVEMENT', b'Achievement')])),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
                ('category', models.CharField(max_length=25, null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='CustomerClassificationJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('crm_id', models.CharField(max_length=100, null=True, blank=True)),
                ('classification', models.ForeignKey(related_name='classification_join', to='mainsite.CustomerClassification')),
                ('customer', models.ForeignKey(related_name='classification_customer', to='mainsite.Customer')),
            ],
            options={
                'db_table': 'mainsite_customer_classifications',
            },
        ),
        migrations.CreateModel(
            name='CustomerSubscription',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='CustomerSubscriptionJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('crm_id', models.CharField(max_length=100, null=True, blank=True)),
                ('customer', models.ForeignKey(related_name='subscription_customer', to='mainsite.Customer')),
                ('subscription', models.ForeignKey(related_name='subscription_join', to='mainsite.CustomerSubscription')),
            ],
            options={
                'db_table': 'mainsite_customer_subscriptions',
            },
        ),
        migrations.CreateModel(
            name='TextPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('txt', ckeditor.fields.RichTextField(max_length=1000, verbose_name=b'Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TextWithClass',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('txt', ckeditor.fields.RichTextField(max_length=1000, verbose_name=b'Text')),
                ('cls', models.CharField(max_length=40, verbose_name=b'Class')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Tier1Discipline',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('crm_code', models.CharField(max_length=20, null=True, verbose_name=b'CRM code', blank=True)),
                ('eva_code', models.CharField(max_length=100, null=True, verbose_name=b'EVA code', blank=True)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Discipline',
            },
        ),
        migrations.CreateModel(
            name='TitleBarPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('discipline', models.ForeignKey(verbose_name=b'Discipline', to='mainsite.Tier1Discipline')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Topic',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='classifications',
            field=models.ManyToManyField(related_name='customers', through='mainsite.CustomerClassificationJoin', to='mainsite.CustomerClassification', blank=True),
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
            field=models.ManyToManyField(related_name='customers', through='mainsite.CustomerSubscriptionJoin', to='mainsite.CustomerSubscription', blank=True),
        ),
    ]
