from django.contrib import admin

from models import EventMenu, MenuItem
from adminsortable.admin import SortableAdmin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from adminsortable.admin import SortableTabularInline


class MenuItemInLine(SortableStackedInline):
    model = MenuItem
    extra =1


class MenuItemTabularInLine(SortableTabularInline):
    model = MenuItem
    extra =1


class EventMenuAdmin(NonSortableParentAdmin):
    inlines = [MenuItemInLine]
    search_fields = ['title']


# class EventMenuCompactAdmin(NonSortableParentAdmin):
#     inlines = [MenuItemTabularInLine]
#     search_fields = ['title']



admin.site.register(EventMenu, EventMenuAdmin)
# admin.site.register(EventMenu, EventMenuCompactAdmin)
admin.site.register(MenuItem, SortableAdmin)

