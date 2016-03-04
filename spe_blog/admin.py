from django.contrib import admin

from .models import Article, Category, Publication
from mainsite.models import Tier1Discipline


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tier1Discipline)
admin.site.register(Category)
admin.site.register(Publication)
