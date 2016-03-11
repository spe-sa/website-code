# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('mainsite', '0006_auto_20160310_2126'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='textplugin',
            name='txt',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name=b'Text'),
        ),
    ]
