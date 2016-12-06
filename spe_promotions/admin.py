# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# from .models import Promotion, SimpleEventPromotion
from .models import (
    SimpleEventPromotion,
    SimpleEventNonMemberMessage,
    SimpleEventMemberMissingDisciplineMessage,
    SimpleEventMemberMissingRegionMessage,
)


class SimpleEventPromotionAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')
    exclude = ['latitude', 'longitude']


class NonMemberMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')

class MemberNoDisciplineMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')

class MemberNoRegionMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')


# admin.site.register(Promotion)
admin.site.register(SimpleEventPromotion, SimpleEventPromotionAdmin)
admin.site.register(SimpleEventNonMemberMessage, NonMemberMessageAdmin)
admin.site.register(SimpleEventMemberMissingDisciplineMessage, MemberNoDisciplineMessageAdmin)
admin.site.register(SimpleEventMemberMissingRegionMessage, MemberNoRegionMessageAdmin)
