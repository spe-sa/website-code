from django.contrib import admin

from .models import Article, Category, Publication, Issue
from mainsite.models import Tier1Discipline


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['auto_tags']
    filter_horizontal = ('topics', )

#    def get_form(self, request, obj=None, **kwargs):
#        if obj and obj.free:
#            self.exclude = []
#        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tier1Discipline)
admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Issue)
