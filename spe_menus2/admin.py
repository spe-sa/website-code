from django.contrib import admin
# from adminsortable2.admin import SortableAdminMixin
# from models import MenuItem

# class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
#     pass
# admin.site.register(MenuItem, MyModelAdmin)

from adminsortable.admin import SortableAdmin

# from models import EventMenu, MenuItem, MenuLevel1, MenuLevel2
from models import EventMenu, MenuItem
from adminsortable.admin import SortableAdmin
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from adminsortable.admin import SortableTabularInline

# class MenuLevel1Admin(SortableAdmin):
#     search_fields = ['event__title']


class MenuItemInLine(SortableStackedInline):
    model = MenuItem
    extra =1


class EventMenuAdmin(NonSortableParentAdmin):
    inlines = [MenuItemInLine]
    search_fields = ['title']


# class MenuLevel2Inline(SortableStackedInline):
#     model = MenuLevel2
#     extra = 1
#
# class MenuLevel1Inline(SortableStackedInline):
#     model = MenuLevel1
#     extra = 1
#     # inlines = [MenuLevel2Inline]
#
# class EventMenuAdmin(NonSortableParentAdmin):
#     inlines = [MenuLevel1Inline]
#     search_fields = ['title']

admin.site.register(EventMenu, EventMenuAdmin)
admin.site.register(MenuItem, SortableAdmin)
# admin.site.register(MenuLevel1, MenuLevel1Admin)
# admin.site.register(MenuLevel1, SortableAdmin)
# admin.site.register(MenuLevel2, SortableAdmin)
