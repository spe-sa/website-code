from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.geoip import GeoIP

# from .models import ArticleDisciplineByUserPluginModel
# from .models import ArticleDisciplinePluginModel
# from .models import ArticleByPublicationPluginModel
# from .models import SelectedFeatureArticlePluginModel
from .models import Article, ArticlesPlugin, ArticlesListingPlugin, Issue, IssuesByPublicationPlugin
from .forms import ArticleSelectionForm



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


# class ShowArticlePlugin(ArticlePluginBase):
#     model = ArticlesPlugin
#     name = _("Selected Article ")
#
#     def render(self, context, instance, placeholder):
#         queryset = Article.objects.filter(id=instance.article.id)
#         context.update({'articles': queryset})
#         context.update({'show_all_url': instance.all_url})
#         context.update({'show_all_text': instance.all_text})
#         self.render_template = instance.template
#         return context


class ShowArticlesPlugin(ArticlePluginBase):
    model = ArticlesPlugin
    name = _("Selected Articles ")
    form = ArticleSelectionForm

    def render(self, context, instance, placeholder):
        queryset = Article.objects.filter(id__in=instance.articles.all()).order_by(instance.order_by)
        context.update({'articles': queryset})
        context.update({'show_all_url': instance.all_url})
        context.update({'show_all_text': instance.all_text})
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

class ShowMeetingByUserPlugin(CMSPluginBase):
    model = CMSPlugin
    allow_children = False
    cache = False
    module = _('Personalize')
    name = _('Meetings Near You')
    text_enabled = False
    render_template = 'spe_blog/plugins/location.html'
    #render_plugin = False

    def render(self, context, instance, placeholder):
        g = GeoIP()
        ip = context['request'].META.get('REMOTE_ADDR', None) 
        if ip:
            loc = g.city(ip)
        else:
            loc = None
        #loc = g.city('google.com')
        context.update({'location': loc})
        #return HttpResponse(json.dumps([current_location['country_code3']]))
        return context

class ShowIssuesByPublicationPlugin(CMSPluginBase):
    model = IssuesByPublicationPlugin
    allow_children = False
    cache = False
    module = _('Publications')
    name = _('Issues by Publication Listing')
    text_enabled = False
    render_template = 'spe_blog/plugins/issues.html'
    #render_plugin = False

    def render(self, context, instance, placeholder):
        queryset = Issue.objects.filter(publication=instance.publication).order_by('-date')[instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        context.update({'issues': queryset})
        context.update({'show_all_url': instance.all_url})
        context.update({'show_all_text': instance.all_text})
        self.render_template = instance.template
        return context


# plugin_pool.register_plugin(ShowArticlePlugin)
plugin_pool.register_plugin(ShowArticlesPlugin)
plugin_pool.register_plugin(ShowArticlesListingPlugin)
# plugin_pool.register_plugin(ShowArticlesByUserDisciplinePlugin)
# plugin_pool.register_plugin(ShowArticlesByDisciplinePlugin)
# plugin_pool.register_plugin(ShowArticlesFromPublicationPlugin)
# plugin_pool.register_plugin(ShowFeatureArticlesPlugin)
plugin_pool.register_plugin(ShowMeetingByUserPlugin)
plugin_pool.register_plugin(ShowIssuesByPublicationPlugin)
