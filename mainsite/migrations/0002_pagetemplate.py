# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_page', models.CharField(default=b'WWW', max_length=255, choices=[(b'WWW', b'Web Page'), (b'JPT', b'Journal of Petroleum Technology'), (b'TWA', b'The Way Ahead'), (b'OGF', b'Oil and Gas Facilities'), (b'HSE', b'HSE Now')])),
                ('template', models.CharField(default=b'3Column.html', max_length=255, choices=[(b'3Column.html', b'Three Column'), (b'2Column.html', b'Two Column'), (b'1Column.html', b'Single Column')])),
            ],
        ),
    ]
