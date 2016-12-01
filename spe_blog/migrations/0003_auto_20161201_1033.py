# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_blog', '0002_auto_20161129_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brieflistingplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/brief_interest.html', max_length=255, choices=[(b'spe_blog/plugins/brief_index.html', b'Index listing'), (b'spe_blog/plugins/brief_accordion.html', b'POI Accordion Listing'), (b'spe_blog/plugins/side_list.html', b'Brief List'), (b'spe_blog/plugins/brief_list_pics.html', b'Brief List with Images'), (b'spe_blog/plugins/best_shot_1.html', b'Best Shot 1 Col'), (b'spe_blog/plugins/best_shot_2.html', b'Best Shot 2 Col'), (b'spe_blog/plugins/best_shot.html', b'Best Shot 3 Col'), (b'spe_blog/plugins/brief_interest_widepics.html', b'Brief of interest listing Wide Pics'), (b'spe_blog/plugins/brief_interest.html', b'Brief of interest listing')]),
        ),
        migrations.AlterField(
            model_name='briefplugin',
            name='template',
            field=models.CharField(default=b'spe_blog/plugins/brief_interest.html', max_length=255, choices=[(b'spe_blog/plugins/brief_index.html', b'Index listing'), (b'spe_blog/plugins/brief_accordion.html', b'POI Accordion Listing'), (b'spe_blog/plugins/side_list.html', b'Brief List'), (b'spe_blog/plugins/brief_list_pics.html', b'Brief List with Images'), (b'spe_blog/plugins/best_shot_1.html', b'Best Shot 1 Col'), (b'spe_blog/plugins/best_shot_2.html', b'Best Shot 2 Col'), (b'spe_blog/plugins/best_shot.html', b'Best Shot 3 Col'), (b'spe_blog/plugins/brief_interest_widepics.html', b'Brief of interest listing Wide Pics'), (b'spe_blog/plugins/brief_interest.html', b'Brief of interest listing')]),
        ),
    ]
