from django.contrib import admin
from adminsortable.admin import SortableAdmin, NonSortableParentAdmin, SortableStackedInline

from models import Event, SponsorCategory, Sponsor

class SponsorCategoryInLine(SortableStackedInline):
    model = SponsorCategory
    extra = 1

class SponsorEventAdmin(NonSortableParentAdmin):
    inlines = [SponsorCategoryInLine]

admin.site.register(Sponsor)
admin.site.register(Event, SponsorEventAdmin)