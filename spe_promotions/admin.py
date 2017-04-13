# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# from .models import Promotion, SimpleEventPromotion
from .models import (
    SimpleEventPromotion,
    SimpleEventNotLoggedInPromotion,
    SimpleEventNonMemberPromotion,
    SimpleEventNoDisciplinePromotion,
    SimpleEventNoAddressPromotion,
    SimpleMembershipPromotion,
)


def blank_timezone(modeladmin, request, queryset):
    for x in queryset.all():
        x.event_tz = None
        x.save()


blank_timezone.short_description = "Blank Time Zones"


class SimpleEventPromotionAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end', 'event_type__name')
    exclude = ['latitude', 'longitude']
    readonly_fields = ['hits', 'impressions', 'last_impression']
    actions = [blank_timezone, ]


class NotLoggedInMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')
    readonly_fields = ['hits', 'impressions', 'last_impression']


class NonMemberMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')
    readonly_fields = ['hits', 'impressions', 'last_impression']


class MemberNoDisciplineMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')
    readonly_fields = ['hits', 'impressions', 'last_impression']


class MemberNoRegionMessageAdmin(admin.ModelAdmin):
    search_fields = ('event', 'start', 'end')
    readonly_fields = ['hits', 'impressions', 'last_impression']


class SimpleMembershipPromotionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'start', 'end')
    readonly_fields = ['hits', 'impressions', 'last_impression']



# class ReadOnlyAdmin(admin.ModelAdmin):
#     readonly_fields = []
#
#     def get_readonly_fields(self, request, obj=None):
#         return list(self.readonly_fields) + \
#                [field.name for field in obj._meta.fields]
#
#     def has_add_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#
# # Create a read only view of Promotion Clicks
# class PromotionsEventClicksAdmin(ReadOnlyAdmin):
#     pass


admin.site.register(SimpleEventPromotion, SimpleEventPromotionAdmin)
admin.site.register(SimpleEventNotLoggedInPromotion, NotLoggedInMessageAdmin)
admin.site.register(SimpleEventNonMemberPromotion, NonMemberMessageAdmin)
admin.site.register(SimpleEventNoDisciplinePromotion, MemberNoDisciplineMessageAdmin)
admin.site.register(SimpleEventNoAddressPromotion, MemberNoRegionMessageAdmin)
admin.site.register(SimpleMembershipPromotion, SimpleMembershipPromotionAdmin)
