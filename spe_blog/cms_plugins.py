#from itertools import chain
import requests
import json
import re
from urlparse import urlparse, parse_qs

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils import timezone

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.geoip import GeoIP

# from .models import ArticleDisciplineByUserPluginModel
# from .models import ArticleDisciplinePluginModel
# from .models import ArticleByPublicationPluginModel
# from .models import SelectedFeatureArticlePluginModel
from .models import (
    Article, ArticlesPlugin, ArticlesListingPlugin, ArticleDetailPlugin,
    Issue, IssuesByPublicationPlugin, 
    Editorial, EditorialPlugin, Publication,
    IssuesByYearPlugin
)
from .forms import ArticleSelectionForm, EditorialSelectionForm
import sys


class ArticlePluginBase(CMSPluginBase):
    """
    Abstract base class to be used for all Article plugins.
    """

    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = _('Article')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False


class ShowArticleDetailPlugin(ArticlePluginBase):
     model = ArticleDetailPlugin
     name = _("Show Article Detail")

     def render(self, context, instance, placeholder):
         now = timezone.now()
         art = get_object_or_404(Article, pk=instance.article.id)
         if instance.allow_url_to_override_selection:
             q = re.findall('(art)=(\d+)', urlparse(context.get('request').get_full_path()).query)
             if q and q[0][0] == 'art':
                 pk = int(q[0][1])
                 if pk:
                     try:
                         art = get_object_or_404(Article, pk=pk)
                     except:
                         raise Http404("Article not found")
         context.update({'article': art})
         context.update({'dateNow': now})
         self.render_template = 'spe_blog/plugins/article_detail.html' 
         return context


class ShowArticlesPlugin(ArticlePluginBase):
    model = ArticlesPlugin
    name = _("Selected Articles ")
    form = ArticleSelectionForm

    def render(self, context, instance, placeholder):
#        if instance.keep_original_order:
#            queryset = Article.objects.none()
#            for art in instance.articles.all():
#                queryadd = Article.objects.filter(id=art.id).all()
#                queryset = list(chain(queryset, queryadd))
#        else:
#            queryset = Article.objects.filter(id__in=instance.articles.all()).order_by(instance.order_by)
        queryset = Article.objects.filter(id__in=instance.articles.all()).order_by(instance.order_by)
        context.update({'articles': queryset})
        context.update({'show_all_url': instance.all_url})
        context.update({'show_all_text': instance.all_text})
        self.render_template = instance.template
        return context

class ShowEditorialPlugin(ArticlePluginBase):
    model = EditorialPlugin
    name = _("Editorial")
    form = EditorialSelectionForm

    def render(self, context, instance, placeholder):
        queryset = Editorial.objects.filter(id__in=instance.editorial.all())
        context.update({'editorials': queryset})
        context.update({'link': instance.lnk})
        self.render_template = instance.template
        return context

class ShowArticlesListingPlugin(ArticlePluginBase):
    model = ArticlesListingPlugin
    name = _("Articles Listing")

    def render(self, context, instance, placeholder):
        request = context.get('request')
        # NOTE: change this to be set in the context globally and stored server side
        ducode = None
        dcode = None
        if instance.personalized:
            ducode = request.COOKIES.get('dc')
        if instance.discipline:
            dcode = instance.discipline.code
        context.update({'ducode': ducode, 'dcode': dcode})
        # NOTE: todo - create an in clause filter with each code if there are any
        if instance.publication:
            qs = Article.objects.filter(publication=instance.publication)
        else:
            qs = Article.objects.all()

        if instance.category:
            qs = qs.filter(category=instance.category)

        if ducode:
            qs = qs.filter(disciplines=ducode).order_by(instance.order_by)[instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        elif dcode:
            qs = qs.filter(disciplines=dcode).order_by(instance.order_by)[instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        else:
            qs = qs.order_by(instance.order_by)[instance.starting_with - 1:instance.cnt]
        # NOTE: add other querysets if the publication and discipline is set; need 1 for each combination
        context.update({'articles': qs})
        self.render_template = instance.template
        return context


# class ShowArticlesByUserDisciplinePlugin(ArticlePluginBase):
#     model = ArticleDisciplineByUserPluginModel
#     name = _("Show Articles by User Discipline")
#
#     def render(self, context, instance, placeholder):
#         dc = context.get('request').COOKIES.get("dc")
#         queryset = Article.objects.filter(disciplines=dc).order_by(instance.orderby)[
#                    instance.starting_with:instance.articles]
#         context.update({'articles': queryset})
#         context.update({'title': instance.title})
#         return context
#
#
# class ShowArticlesByDisciplinePlugin(ArticlePluginBase):
#     model = ArticleDisciplinePluginModel
#     name = _("Show Articles by Discipline")
#
#     def render(self, context, instance, placeholder):
#         queryset = Article.objects.filter(disciplines=instance.discipline.code).order_by(instance.orderby)[
#                    instance.starting_with:instance.articles]
#         context.update({'articles': queryset})
#         context.update({'title': instance.title})
#         return context
#
#
# class ShowArticlesFromPublicationPlugin(ArticlePluginBase):
#     model = ArticleByPublicationPluginModel
#     name = _("Show Articles From Publication")
#
#     def render(self, context, instance, placeholder):
#         queryset = Article.objects.filter(publication=instance.publication).order_by(instance.orderby)[
#                    instance.starting_with:instance.articles]
#         context.update({'articles': queryset})
#         context.update({'title': instance.title})
#         return context
#
#
# class ShowFeatureArticlesPlugin(ArticlePluginBase):
#     model = SelectedFeatureArticlePluginModel
#     name = _("Show Article From Publication")
#
#     def render(self, context, instance, placeholder):
#         queryset = Article.objects.filter(publication=instance.publication).filter(print_issue=instance.issue).filter(
#             slug=instance.slug)
#         if queryset:
#             context.update({'articles': queryset})
#         self.render_template = instance.template
#         return context


class ShowIssuesByPublicationPlugin(CMSPluginBase):
    model = IssuesByPublicationPlugin
    allow_children = False
    cache = False
    module = _('Publications')
    name = _('Issues by Publication Listing')
    text_enabled = False
    render_template = 'spe_blog/plugins/issue_channel.html'
    #render_plugin = False

    def render(self, context, instance, placeholder):
        queryset = Issue.objects.filter(publication=instance.publication).order_by('-date')[instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        context.update({'publication': instance.publication})
        context.update({'issues': queryset})
        context.update({'show_all_url': instance.all_url})
        context.update({'show_all_text': instance.all_text})
        context.update({'show_subscribe_url': instance.publication.subscription_url})
        self.render_template = instance.template
        return context

# class ShowBreadCrumbPlugin(CMSPluginBase):
#     model = BreadCrumbPlugin
#     allow_children = False
#     cache = False
#     module = _('Publications')
#     name = _('Bread Crumb')
#     text_enabled = False
#     render_template = 'spe_blog/plugins/bread_crumb.html'
#
#     def render(self, context, instance, placeholder):
#         context.update({'title': instance.title})
#         return context

class ShowIssuesByYearPlugin(CMSPluginBase):
    model = IssuesByYearPlugin
    allow_children = False
    cache = False
    module = _('Publications')
    name = _('Issues by Year')
    text_enabled = False
    render_template = 'spe_blog/plugins/issues_by_year.html'

    def render(self, context, instance, placeholder):
        issues = Issue.objects.filter(publication=instance.publication).order_by('-date')
        context.update({'issues': issues})
        return context

plugin_pool.register_plugin(ShowArticleDetailPlugin)
plugin_pool.register_plugin(ShowArticlesPlugin)
plugin_pool.register_plugin(ShowEditorialPlugin)
plugin_pool.register_plugin(ShowArticlesListingPlugin)
plugin_pool.register_plugin(ShowIssuesByPublicationPlugin)
# plugin_pool.register_plugin(ShowBreadCrumbPlugin)
plugin_pool.register_plugin(ShowIssuesByYearPlugin)
