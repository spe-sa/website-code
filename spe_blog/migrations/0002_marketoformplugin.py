# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('spe_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketoFormPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description of form')),
                ('thank_you', models.CharField(max_length=200, verbose_name=b'Confirmation text')),
                ('marketo_form', models.PositiveIntegerField(verbose_name=b'Marketo form code')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
