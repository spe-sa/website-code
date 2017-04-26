# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Article, Category, SecondaryCategory, Publication, Issue, Editorial
from .models import Brief, ArticleDetailPage, BriefDetailPage, TopicsPage, TagsPage, Blog


# from mainsite.models import Tier1Discipline


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['auto_tags']
    readonly_fields = ['article_hits', 'article_last_viewed', ]
    filter_horizontal = ('topics',)
    fieldsets = (
        (None, {
            'fields': (
                'publication', 'print_volume', 'print_issue', 'sponsored', 'onlineonly', 'category', 'secondary_category', 'title',
                'slug', 'teaser',
                'author', 'introduction', 'article_text', 'date', 'disciplines', 'topics', 'tags'
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
        (_('Editorial'), {
            'classes': ('collapse',),
            'fields': (
                'editorial_title',
                'author_name',
                'author_title',
                'author_picture',
                # 'author_picture_alternate',
                # 'author_picture_attribution',
                # 'author_picture_caption',
                'author_bio',
            ),
        }),
        (_('Free'), {
            'classes': ('collapse',),
            'fields': (
                'free',
                ('free_start', 'free_stop'),
            ),
        }),
        (_('Tracking'), {
            'classes': ('collapse',),
            'fields': (
                ('article_hits', 'article_last_viewed'),
            ),
        }),
    )


class ArticleEditor(Article):
    class Meta:
        proxy = True
        verbose_name_plural = "articles (editor view)"


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)


make_published.short_description = "Mark selected as published"


class ArticleEditorAdmin(ArticleAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['auto_tags']
    filter_horizontal = ('topics',)
    list_filter = ('published', 'date', )
    fieldsets = (
        (None, {
            'fields': (
                'publication', 'print_volume', 'print_issue', 'sponsored', 'onlineonly', 'category', 'secondary_category', 'title',
                'slug', 'teaser',
                'author', 'introduction', 'article_text', 'date', 'disciplines', 'topics', 'tags'
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
        (_('Editorial'), {
            'classes': ('collapse',),
            'fields': (
                'editorial_title',
                'author_name',
                'author_title',
                'author_picture',
                'author_bio',
            ),
        }),
        (_('Free'), {
            'classes': ('collapse',),
            'fields': (
                'free',
                ('free_start', 'free_stop'),
            ),
        }),
        (_('Tracking'), {
            'classes': ('collapse',),
            'fields': (
                ('article_hits', 'article_last_viewed'),
            ),
        }),
        (None, {
            'fields': (
                'published',
            ),
        }),
    )
    actions = [make_published]


class BriefAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['auto_tags']
    readonly_fields = ['article_hits', 'article_last_viewed', ]
    filter_horizontal = ('topics',)
    fieldsets = (
        (None, {
            'fields': (
                'publication', 'onlineonly', 'print_volume', 'print_issue', 'category', 'secondary_category', 'title', 'slug',
                'author', 'article_text', 'date', 'topics', 'region', 'tags'
            ),
        }),
        (_('Image'), {
            'classes': ('collapse',),
            'fields': (
                'picture',
                'picture_alternate',
            ),
        }),
        (_('Free'), {
            'classes': ('collapse',),
            'fields': (
                'free',
                ('free_start', 'free_stop'),
            ),
        }),
        (_('Tracking'), {
            'classes': ('collapse',),
            'fields': (
                ('article_hits', 'article_last_viewed'),
            ),
        }),
    )


class BriefEditor(Brief):
    class Meta:
        proxy = True
        verbose_name_plural = "briefs (editor view)"


class BriefEditorAdmin(BriefAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['auto_tags']
    filter_horizontal = ('topics',)
    list_filter = ('published', 'date', )
    fieldsets = (
        (None, {
            'fields': (
                'publication', 'onlineonly', 'print_volume', 'print_issue', 'category', 'secondary_category', 'title', 'slug',
                'author', 'article_text', 'date', 'topics', 'region', 'tags'
            ),
        }),
        (_('Image'), {
            'classes': ('collapse',),
            'fields': (
                'picture',
                'picture_alternate',
            ),
        }),
        (_('Free'), {
            'classes': ('collapse',),
            'fields': (
                'free',
                ('free_start', 'free_stop'),
            ),
        }),
        (_('Tracking'), {
            'classes': ('collapse',),
            'fields': (
                ('article_hits', 'article_last_viewed'),
            ),
        }),
        (None, {
            'fields': (
                'published',
            ),
        }),
    )
    actions = [make_published]


# def get_form(self, request, obj=None, **kwargs):
#        if obj and obj.free:
#            self.exclude = []
#        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(ArticleEditor, ArticleEditorAdmin)
admin.site.register(Brief, BriefAdmin)
admin.site.register(BriefEditor, BriefEditorAdmin)
admin.site.register(Editorial)
admin.site.register(Category)
admin.site.register(SecondaryCategory)
admin.site.register(Publication)
admin.site.register(Issue)
admin.site.register(ArticleDetailPage)
admin.site.register(BriefDetailPage)
admin.site.register(TopicsPage)
admin.site.register(TagsPage)
