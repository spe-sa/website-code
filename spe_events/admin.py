from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import EventType, EventMenuModel

class SortableEventMenu(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['event_code', ]

admin.site.register(EventType)
admin.site.register(EventMenuModel, SortableEventMenu)
