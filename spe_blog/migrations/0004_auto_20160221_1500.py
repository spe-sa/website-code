# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0003_auto_20160221_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedfeaturearticlepluginmodel',
            name='template',
            field=models.CharField(max_length=255, verbose_name=b'Feature type', choices=[(b'spe_blog/plugins/image_left.html', b'Image on left'), (b'spe_blog/plugins/overlay.html', b'Image with caption overlay')]),
        ),
    ]
