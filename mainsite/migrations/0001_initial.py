# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mainsite.models
import filer.fields.image
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('filer', '0004_auto_20160328_1434'),
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
            name='Countries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(unique=True, max_length=50)),
                ('country_ISO', models.CharField(unique=True, max_length=2)),
                ('country_UN', models.CharField(unique=True, max_length=3)),
                ('country_UN_number', models.PositiveIntegerField()),
                ('country_dial_code', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['country_name'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
                ('prefix', models.CharField(max_length=50, null=True, blank=True)),
                ('suffix', models.CharField(max_length=20, null=True, blank=True)),
                ('first_name', models.CharField(db_index=True, max_length=80, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=60, null=True, blank=True)),
                ('last_name', models.CharField(db_index=True, max_length=60, null=True, blank=True)),
                ('nickname', models.CharField(max_length=80, null=True, blank=True)),
                ('formal_salutation', models.CharField(max_length=180, null=True, blank=True)),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, blank=True)),
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
            name='MarketoFormPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('instructions', models.CharField(max_length=200, verbose_name=b'Instructions for form')),
                ('thank_you', models.CharField(max_length=200, verbose_name=b'Confirmation text')),
                ('marketo_form', models.PositiveIntegerField(verbose_name=b'Marketo form code')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_code', models.CharField(unique=True, max_length=15)),
                ('region_name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['region_code'],
                'verbose_name': 'Region',
            },
        ),
        migrations.CreateModel(
            name='TextPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('txt', ckeditor_uploader.fields.RichTextUploadingField(help_text='Text', max_length=50000)),
                ('cls', models.CharField(default=b'tile-white', max_length=40, verbose_name=b'Class', choices=[(b'tile-alert', b'Alert Box'), (b'tile-blue', b'Blue Box'), (b'tile-greenbar', b'White Box - Green Bar'), (b'tile-bluebar', b'White Box - Blue Bar'), (b'tile-white', b'White Box')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Tier1Discipline',
            fields=[
                ('code', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('crm_code', models.CharField(max_length=50, null=True, verbose_name=b'CRM code', blank=True)),
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
            name='TileImgBack',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('ttl', models.CharField(max_length=250, verbose_name=b'Title')),
                ('txt', ckeditor_uploader.fields.RichTextUploadingField(help_text='Text Area', max_length=2000)),
                ('lnk', models.URLField(max_length=250, verbose_name=b'Link')),
                ('date', models.DateField(null=True, blank=True)),
                ('img', filer.fields.image.FilerImageField(related_name='background_picture', verbose_name='Background Image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TitleBarPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=100)),
                ('backcol', mainsite.models.ColorField(max_length=10, null=True, verbose_name=b'Background Color', blank=True)),
                ('textcol', mainsite.models.ColorField(max_length=10, null=True, verbose_name=b'Text Color', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Topic',
            },
        ),
        migrations.CreateModel(
            name='Web_Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_code', models.CharField(unique=True, max_length=15)),
                ('region_name', models.CharField(unique=True, max_length=50)),
                ('is_visible', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['region_name'],
            },
        ),
        migrations.CreateModel(
            name='Web_Region_Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_UN', models.CharField(max_length=25, verbose_name=b'Country Code')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='mainsite.Web_Region', null=True)),
            ],
            options={
                'verbose_name': 'Web Region Country',
                'verbose_name_plural': 'Web Region Countries',
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
            field=models.ForeignKey(related_name='primary_customers', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='secondary_discipline',
            field=models.ForeignKey(related_name='secondary_customers', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Tier1Discipline', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='subscriptions',
            field=models.ManyToManyField(related_name='customers', through='mainsite.CustomerSubscriptionJoin', to='mainsite.CustomerSubscription', blank=True),
        ),
        migrations.AddField(
            model_name='countries',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='mainsite.Regions', null=True),
        ),
    ]
