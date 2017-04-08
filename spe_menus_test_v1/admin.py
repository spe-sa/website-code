from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from models import MenuItem

class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(MenuItem, MyModelAdmin)