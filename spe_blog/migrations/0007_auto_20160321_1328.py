# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0006_auto_20160319_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to=b'regular_images', verbose_name='Picture for article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text=b'SEO Friendly name that is unique for use in URL', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('publication', 'print_volume', 'print_issue', 'slug', 'date')]),
        ),
    ]
