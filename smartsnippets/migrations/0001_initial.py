# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartSnippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('template_code', models.TextField(verbose_name='Template code', blank=True)),
                ('template_path', models.CharField(help_text='Enter a template (i.e. "snippets/plugin_xy.html") which will be rendered.', max_length=100, verbose_name='Template path', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('documentation_link', models.CharField(help_text='Enter URL (i.e. "http://snippets/docs/plugin_xy.html") to the extended documentation.', max_length=100, verbose_name='Documentation link', blank=True)),
                ('sites', models.ManyToManyField(help_text='Select on which sites the snippet will be available.', to='sites.Site', verbose_name=b'sites', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Smart Snippet',
                'verbose_name_plural': 'Smart Snippets',
            },
        ),
        migrations.CreateModel(
            name='SmartSnippetPointer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('snippet', models.ForeignKey(to='smartsnippets.SmartSnippet')),
            ],
            options={
                'db_table': 'cmsplugin_smartsnippetpointer',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SmartSnippetVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter the name of the variable defined in the smart snippet template. Unallowed characters will be removed when the form is saved.', max_length=50)),
                ('widget', models.CharField(help_text='Select the type of the variable defined in the smart snippet template.', max_length=50)),
                ('resources', models.TextField(null=True, verbose_name='Admin resources', blank=True)),
            ],
            options={
                'verbose_name': 'Standard variable',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField()),
                ('snippet', models.ForeignKey(related_name='variables', to='smartsnippets.SmartSnippetPointer')),
            ],
        ),
        migrations.CreateModel(
            name='DropDownVariable',
            fields=[
                ('smartsnippetvariable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='smartsnippets.SmartSnippetVariable')),
                ('choices', models.CharField(help_text='Enter a comma separated list of choices that will be available in the dropdown variable when adding and configuring the smart snippet on a page.', max_length=512)),
            ],
            bases=('smartsnippets.smartsnippetvariable',),
        ),
        migrations.AddField(
            model_name='variable',
            name='snippet_variable',
            field=models.ForeignKey(related_name='variables', to='smartsnippets.SmartSnippetVariable'),
        ),
        migrations.AddField(
            model_name='smartsnippetvariable',
            name='snippet',
            field=models.ForeignKey(related_name='variables', to='smartsnippets.SmartSnippet'),
        ),
        migrations.AlterUniqueTogether(
            name='variable',
            unique_together=set([('snippet_variable', 'snippet')]),
        ),
        migrations.AlterUniqueTogether(
            name='smartsnippetvariable',
            unique_together=set([('snippet', 'name')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='smartsnippetvariable',
            order_with_respect_to='snippet',
        ),
    ]
