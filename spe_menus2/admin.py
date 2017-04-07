from django.contrib import admin

from models import EventMenu, MenuItem
from adminsortable.admin import SortableAdmin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from adminsortable.admin import SortableTabularInline


class MenuItemInLine(SortableStackedInline):
    model = MenuItem
    extra = 1


class MenuItemTabularInLine(SortableTabularInline):
    model = MenuItem
    extra =1
    exclude = ['title', 'level', 'page', 'url', 'transition', 'order']


class EventMenuAdmin(NonSortableParentAdmin):
    inlines = [MenuItemInLine, MenuItemTabularInLine]
    search_fields = ['title']
    class Meta:
        verbose_name_plural = "Event Menus"


admin.site.register(EventMenu, EventMenuAdmin)
admin.site.register(MenuItem, SortableAdmin)
