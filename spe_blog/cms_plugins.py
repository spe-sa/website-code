from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import ArticleDisciplineByUserPluginModel
from .models import ArticleDisciplinePluginModel
from .models import ArticleByPublicationPluginModel
from .models import SelectedFeatureArticlePluginModel
from .models import Article

from cms.plugin_base import CMSPluginBase


class ArticlePluginBase(CMSPluginBase):
    '''
    Abstract base class to be used for all Article plugins. 
    '''

    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = _('Article')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False

class ShowArticlesByUserDisciplinePlugin(ArticlePluginBase):
    model = ArticleDisciplineByUserPluginModel
    name = _("Show Articles by User Discipline")

    def render(self, context, instance, placeholder):
        request = context.get('request')
        value = request.COOKIES.get("discipline")
        queryset = Article.objects.filter(discipline=value).order_by(instance.orderby)[instance.starting_with:instance.articles]
        context.update({ 'articles': queryset })
        context.update({ 'title': instance.title })
        return context

class ShowArticlesByDisciplinePlugin(ArticlePluginBase):
    model = ArticleDisciplinePluginModel
    name = _("Show Articles by Discipline")

    def render(self, context, instance, placeholder):
        queryset = Article.objects.filter(discipline=instance.discipline).order_by(instance.orderby)[instance.starting_with:instance.articles]
        context.update({ 'articles': queryset })
        context.update({ 'title': instance.title })
        return context

class ShowArticlesFromPublicationPlugin(ArticlePluginBase):
    model = ArticleByPublicationPluginModel
    name = _("Show Articles From Publication")

    def render(self, context, instance, placeholder):
        queryset = Article.objects.filter(magazine=instance.magazine).order_by(instance.orderby)[instance.starting_with:instance.articles]
        context.update({ 'articles': queryset })
        context.update({ 'title': instance.title })
        return context

class ShowFeatureArticlesPlugin(ArticlePluginBase):
    model = SelectedFeatureArticlePluginModel
    name = _("Feature Article From Publication")

    def render(self, context, instance, placeholder):
        queryset = Article.objects.filter(magazine=instance.magazine).filter(issue=instance.issue).filter(article_number=instance.article_number)
        if queryset:
            context.update({ 'article': queryset[0] })
        self.render_template = instance.template
        return context

plugin_pool.register_plugin(ShowArticlesByUserDisciplinePlugin)
plugin_pool.register_plugin(ShowArticlesByDisciplinePlugin)
plugin_pool.register_plugin(ShowArticlesFromPublicationPlugin)
plugin_pool.register_plugin(ShowFeatureArticlesPlugin)
