from django.contrib import admin

from .models import EventType, ImageItemList, ImageItems

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline, SortableTabularInline


class ImageItemInLine(SortableStackedInline):
    model = ImageItems
    extra = 0
    fieldsets = (
        ('Detail', {
            'classes': ('collapse',),
            'fields': (
                'title',
                'image',
                'imageposition',
                'text',
                'external_link',
                'internal_link',
                'isvisible',
                'issponsor',
                'sponsorlevel',
                'sponsoredevents',
            ),
        }),
    )
    exclude = ['order']


class ImageItemTabularInLine(SortableTabularInline):
    model = ImageItems
    extra = 0
    proxy = True
    exclude = ['title', 'image', 'imageposition', 'text', 'external_link', 'internal_link', 'issponsor', 'sponsorlevel',
               'sponsoredevents', 'order']


class CustomImageItemAdmin(NonSortableParentAdmin):
    inlines = [ImageItemInLine, ImageItemTabularInLine]
    search_fields = ['title']

    class Meta:
        verbose_name_plural = "Image Item List"


admin.site.register(EventType)
admin.site.register(ImageItemList, CustomImageItemAdmin)
