# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import spe_blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0004_auto_20161115_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='backcol',
            field=spe_blog.models.ColorField(default=b'#ffffff', max_length=10, null=True, verbose_name=b'Background Color (for editorials only.)', blank=True),
        ),
        migrations.AlterField(
            model_name='articleslistingplugin',
            name='whitetext',
            field=models.BooleanField(default=False, verbose_name=b'White Text'),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='backcol',
            field=spe_blog.models.ColorField(default=b'#ffffff', max_length=10, null=True, verbose_name=b'Background Color (for editorials only)', blank=True),
        ),
        migrations.AlterField(
            model_name='articlesplugin',
            name='whitetext',
            field=models.BooleanField(default=False, verbose_name=b'White Text'),
        ),
        migrations.AlterField(
            model_name='brieflistingplugin',
            name='backcol',
            field=spe_blog.models.ColorField(default=b'#ffffff', max_length=10, null=True, verbose_name=b'Background Color', blank=True),
        ),
        migrations.AlterField(
            model_name='brieflistingplugin',
            name='whitetext',
            field=models.BooleanField(default=False, verbose_name=b'White Text'),
        ),
        migrations.AlterField(
            model_name='briefplugin',
            name='backcol',
            field=spe_blog.models.ColorField(default=b'#ffffff', max_length=10, null=True, verbose_name=b'Background Color', blank=True),
        ),
        migrations.AlterField(
            model_name='briefplugin',
            name='whitetext',
            field=models.BooleanField(default=False, verbose_name=b'White Text'),
        ),
        migrations.AlterField(
            model_name='editorialplugin',
            name='backcol',
            field=spe_blog.models.ColorField(default=b'#ffffff', max_length=10, null=True, verbose_name=b'Background Color', blank=True),
        ),
    ]
