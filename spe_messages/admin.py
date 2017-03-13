# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TargetedMessage


class TargetedMessageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'show_start_date', 'show_end_date')
    filter_horizontal = ('show_to',)
    # exclude = ['latitude', 'longitude']
    # readonly_fields = ['hits', 'impressions', 'last_impression']
    # actions = [blank_timezone, ]

admin.site.register(TargetedMessage, TargetedMessageAdmin)
