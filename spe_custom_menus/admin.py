from django.contrib import admin

from models import CustomMenus, CustomMenuItems
from adminsortable.admin import SortableAdmin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from adminsortable.admin import SortableTabularInline


class MenuItemInLine(SortableStackedInline):
    model = CustomMenuItems
    extra = 1


class MenuItemTabularInLine(SortableTabularInline):
    model = CustomMenuItems
    extra = 1
    proxy = True
    exclude = ['title', 'internal_link', 'external_link', 'is_dropdown_node', 'depth', 'escapes', 'order']


class CustomMenuAdmin(NonSortableParentAdmin):
    inlines = [MenuItemInLine, MenuItemTabularInLine]
    search_fields = ['title']
    class Meta:
        verbose_name_plural = "Custom Menus"


admin.site.register(CustomMenus, CustomMenuAdmin)
# admin.site.register(CustomMenuItems, SortableAdmin)
