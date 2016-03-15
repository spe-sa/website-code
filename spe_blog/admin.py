# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Article, Category, Publication, Issue, Editorial
from mainsite.models import Tier1Discipline


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['auto_tags']
    filter_horizontal = ('topics', )
    fieldsets = (
        (None, {
            'fields': (
                'publication', 'print_volume', 'print_issue', 'sponsored', 'category', 'title', 'slug', 'teaser', 'author', 'introduction', 'article_text', 'date', 'disciplines', 'topics', 'tags'
            ),
        }),
        (_('Image'), {
            'classes': ('collapse',),
            'fields': (
                'picture',
                'picture_alternate',
                'picture_attribution',
                'picture_caption',
            ),
        }),
        (_('Free'), {
            'classes': ('collapse',),
            'fields': (
                'free',
                ('free_start', 'free_stop'),
            ),
        }),
    )

#    def get_form(self, request, obj=None, **kwargs):
#        if obj and obj.free:
#            self.exclude = []
#        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Editorial)
admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Issue)
