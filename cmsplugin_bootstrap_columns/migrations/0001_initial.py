# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootstrapColumn',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255)),
                ('mobile_device_width', models.CharField(help_text=b'The column width on\n                                           mobile devices (> 768px)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('small_device_width', models.CharField(help_text=b'The column width on\n                                          small (tablet) devices (768px - 992px\n                                          )', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('medium_device_width', models.CharField(help_text=b'The column width on\n                                           medium (small screen\n                                           computers/laptops) devices (992px -\n                                           1200px) ', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('large_device_width', models.CharField(help_text=b'The column width on\n                                          large devices (1200px and over)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('element_style', models.CharField(help_text=b'HTML styles to be applied to\n                                     this element', max_length=255, null=True, verbose_name=b'Element style', blank=True)),
                ('element_id', models.CharField(help_text=b"ID's to be applied to this\n                                  element", max_length=255, null=True, verbose_name=b"Element ID's", blank=True)),
                ('element_class', models.CharField(help_text=b'classes to be applied to this\n                                     element', max_length=255, null=True, verbose_name=b'Element classes', blank=True)),
                ('hide_on_mobile', models.BooleanField(help_text=b'If selected, this\n                                                 item will not display on\n                                                 mobile devices (> 768px)')),
                ('hide_on_small', models.BooleanField(help_text=b'If selected,\n                                                  this item will not display\n                                                  on small devices (768px -\n                                                  992px)')),
                ('hide_on_medium', models.BooleanField(help_text=b'If selected,\n                                                  this item will not display\n                                                  on medium devices (992px -\n                                                  1200px)')),
                ('hide_on_large', models.BooleanField(help_text=b'If selected,\n                                                  this item will not display\n                                                  on large devices (1200px and\n                                                  over)')),
                ('mobile_device_offset', models.CharField(blank=True, help_text=b'The column offset on\n                                            mobile devices (> 768px)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('small_device_offset', models.CharField(blank=True, help_text=b'The column offset on\n                                           small (tablet) devices (768px -\n                                           992px)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('medium_device_offset', models.CharField(blank=True, help_text=b'The column offset on\n                                            medium (small screen\n                                            computers/laptops) devices (992px -\n                                            1200px) ', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('large_device_offset', models.CharField(blank=True, help_text=b'The column offset on\n                                           large devices (1200px and over)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('mobile_device_pull', models.CharField(blank=True, help_text=b'The column pull on\n                                          mobile devices (> 768px)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('small_device_pull', models.CharField(blank=True, help_text=b'The column pull on\n                                         small (tablet) devices (768px - 992px\n                                         )', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('medium_device_pull', models.CharField(blank=True, help_text=b'The column pull on\n                                          medium (small screen\n                                          computers/laptops) devices (992px -\n                                          1200px) ', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('large_device_pull', models.CharField(blank=True, help_text=b'The column pull on\n                                         large devices (1200px and over)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('mobile_device_push', models.CharField(blank=True, help_text=b'The column push on\n                                          mobile devices (> 768px)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('small_device_push', models.CharField(blank=True, help_text=b'The column push on\n                                         small (tablet) devices (768px - 992px\n                                         )', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('medium_device_push', models.CharField(blank=True, help_text=b'The column push on\n                                          medium (small screen\n                                          computers/laptops) devices (992px -\n                                          1200px) ', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('large_device_push', models.CharField(blank=True, help_text=b'The column push on\n                                         large devices (1200px and over)', max_length=255, choices=[(b'0', b'Not Set'), (b'1', b'1/12'), (b'2', b'2/12'), (b'3', b'3/12'), (b'4', b'4/12'), (b'5', b'5/12'), (b'6', b'6/12'), (b'7', b'7/12'), (b'8', b'8/12'), (b'9', b'9/12'), (b'10', b'10/12'), (b'11', b'11/12'), (b'12', b'12/12')])),
                ('content', cms.models.fields.PlaceholderField(slotname=b'column_placeholder', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BootStrapContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255)),
                ('classes', models.CharField(help_text=b'Classes to be applied to this\n                               element', max_length=255, null=True, verbose_name=b'Element Classes', blank=True)),
                ('element_id', models.CharField(help_text=b"ID's to be applied to this\n                                  element", max_length=255, null=True, verbose_name=b"Element ID's", blank=True)),
                ('element_style', models.CharField(help_text=b'HTML styles to be applied to\n                                     this element', max_length=255, null=True, verbose_name=b'Element style', blank=True)),
                ('is_fluid', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BootstrapRow',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255)),
                ('classes', models.CharField(help_text=b'Classes to be applied to this\n                               element', max_length=255, null=True, verbose_name=b'Element Classes', blank=True)),
                ('element_id', models.CharField(help_text=b"ID's to be applied to this\n                                  element", max_length=255, null=True, verbose_name=b"Element ID's", blank=True)),
                ('element_style', models.CharField(help_text=b'HTML styles to be applied to\n                                     this element', max_length=255, null=True, verbose_name=b'Element style', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
