from django.contrib import admin

from .models import EventType, ImageItemList, ImageItems, CalendarEvent
from .forms import ImageItemInLineForm

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline, SortableTabularInline


class ImageItemInLine(SortableStackedInline):
    model = ImageItems
    form = ImageItemInLineForm
    extra = 0
    fieldsets = (
        ('Detail', {
            'classes': ('collapse',),
            'fields': (
                'title',
                'showtitle',
                'imageurl',
                'image',
                'imageposition',
                'text',
                'external_link',
                'internal_link',
                'new_window',
                'isvisible',
                'issponsor',
                'sponsorlevel',
                'sponsoredevents',
            ),
        }),
    )
    exclude = ['order']

    class Media:
        js=(
            'js/validate_urls.js',
        )


class ImageItemTabularInLine(SortableTabularInline):
    model = ImageItems
    extra = 0
    proxy = True
    exclude = ['title', 'imageurl', 'image', 'imageposition', 'text', 'external_link', 'internal_link', 'new_window',
               'issponsor', 'sponsorlevel', 'sponsoredevents', 'order']


class CustomImageItemAdmin(NonSortableParentAdmin):
    inlines = [ImageItemInLine, ImageItemTabularInLine]
    search_fields = ['title']

    class Meta:
        verbose_name_plural = "Image Item List"

    class Media:
        css = {
            'all': ('admin/css/base.css',)
        }


admin.site.register(EventType)
admin.site.register(CalendarEvent)
admin.site.register(ImageItemList, CustomImageItemAdmin)
