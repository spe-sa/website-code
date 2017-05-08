from django.contrib import admin

from models import CustomAgenda, CustomAgendaItems


class AgendaItemInLine(admin.StackedInline):
    model = CustomAgendaItems
    extra = 0
    fieldsets = (
        ('Detail', {
            'classes': ('collapse',),
            'fields': (
                'title',
                'start_date',
                'start_time',
                'end_time',
                'session_description',
            ),
        }),
    )


class CustomAgendaAdmin(admin.ModelAdmin):
    inlines = [AgendaItemInLine, ]
    search_fields = ['title']

    class Meta:
        verbose_name_plural = "Custom Menus"


admin.site.register(CustomAgenda, CustomAgendaAdmin)
