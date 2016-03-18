# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spe_styledlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styledlink',
            name='styles',
            field=models.ManyToManyField(related_name='styled_link_style', default=None, to='spe_styledlink.StyledLinkStyle', blank=True, help_text='Optional. Choose one or more styles for this link.', verbose_name='link style'),
        ),
    ]
