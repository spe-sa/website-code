from django.contrib import admin

from models import CustomAgenda, CustomAgendaItems


class AgendaItemInLine(admin.StackedInline):
    model = CustomAgendaItems
    extra = 1


class CustomAgendaAdmin(admin.ModelAdmin):
    inlines = [AgendaItemInLine, ]
    search_fields = ['title']

    class Meta:
        verbose_name_plural = "Custom Menus"


admin.site.register(CustomAgenda, CustomAgendaAdmin)
