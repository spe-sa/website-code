# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# from .models import Promotion, SimpleEventPromotion
from .models import (
    SimpleEventPromotion,
    SimpleEventNonMemberPromotion,
    SimpleEventNoDisciplinePromotion,
    SimpleEventNoAddressPromotion,
    PromotionsEventClicks,
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
admin.site.register(SimpleEventNonMemberPromotion, NonMemberMessageAdmin)
admin.site.register(SimpleEventNoDisciplinePromotion, MemberNoDisciplineMessageAdmin)
admin.site.register(SimpleEventNoAddressPromotion, MemberNoRegionMessageAdmin)

admin.site.register(PromotionsEventClicks)

