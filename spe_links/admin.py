from django.contrib import admin

# Register your models here.

from .models import *


class SpeLinkAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')

admin.site.register(SpeLinkCategory)
admin.site.register(SpeLink, SpeLinkAdmin)
