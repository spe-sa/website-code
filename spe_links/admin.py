from django.contrib import admin

# Register your models here.

from .models import *
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline

class PageLinkSetTabularInLine(SortableTabularInline):
    model = PageLink
    extra = 1
    proxy = True
    exclude = ['order']


class PageLinkSetAdmin(NonSortableParentAdmin):
    inlines = [PageLinkSetTabularInLine]
    search_fields = ['title']

    class Meta:
        verbose_name_plural = "List of Links"


class SpeLinkAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')

admin.site.register(PageLinkSet, PageLinkSetAdmin)
admin.site.register(SpeLinkCategory)
admin.site.register(SpeLink, SpeLinkAdmin)
