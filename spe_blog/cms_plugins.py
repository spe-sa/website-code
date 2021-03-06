# from itertools import chain
# import requests
# import json
import re
import urlparse
from datetime import datetime
from datetime import timedelta
from itertools import chain
from operator import attrgetter

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.db import connection
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# from cms.models.pluginmodel import CMSPlugin
# from django.contrib.gis.geoip import GeoIP
from taggit.models import Tag

from mainsite.common import (
    get_context_variable,
    get_visitor, get_ip)
from .forms import (
    ArticleSelectionForm,
    BriefSelectionForm,
    ArticleAndBriefSelectionForm,
    EditorialSelectionForm,
    TopicsListSelectionForm,
    BriefsListSelectionForm,
    ArticlesListSelectionForm,
    BlogSelectionForm
)
from .models import (
    Article, ArticlesPlugin, ArticlesListingPlugin, ArticleDetailPlugin, ArticleViews,
    Brief, BriefPlugin, BriefListingPlugin, BriefDetailPlugin, BriefViews, TagsDetailPlugin,
    ArticleAndBriefMixPlugin,
    Issue, IssuesByPublicationPlugin,
    Editorial, EditorialPlugin,
    BreadCrumbPlugin,
    # Publication,
    IssuesByYearPlugin, IssueCoverPlugin,
    TopicsListPlugin, TopicsPlugin, Topics,
    BlogPluginModel, BlogListingPluginModel, Blog
)

# from netaddr import IPAddress

exclude_agents = ['bot', 'spider', 'crawl', 'search', 'python', 'miketest', '8legs', 'ltx71', 'icevikatam', 'goldfire',
                  'fetch', 'archive', 'metauri', 'go-http-client', 'jetty', 'java', 'php', 'drupal', 'coldfusion',
                  'idg/uk', 'default', 'downnotifier', 'jakarta', 'grammarly', 'check', 'scoutjet']


def getPublicationCode(pub):
    if pub:
        return pub.code
    return ""


class BlogPluginBase(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = True
    module = _('Article')
    text_enabled = False
    render_template = 'spe_blog/plugins/blog_posts.html'


class BlogDetailPlugin(BlogPluginBase):
    name = _("Blog Details")
    module = _('Article Page Components')

    def render(self, context, instance, placeholder):
        now = timezone.now()
        request = context.get('request')
        # get our slug if one was passed.  if not set to None
        slug = get_context_variable(request, "id")
        # get our look and feel if passed, otherwise default to WWW
        laf = get_context_variable(request, "laf", "WWW")
        blog = get_object_or_404(Blog, slug=slug)
        context.update({'blog': blog})
        context.update({'slug': slug})
        context.update({'laf': laf})
        self.render_template = 'spe_blog/plugins/blog_detail.html'
        return context


class BlogPlugin(BlogPluginBase):
    model = BlogPluginModel
    name = _('Selected Blog Posts')
    form = BlogSelectionForm

    def render(self, context, instance, placeholder):
        queryset = Blog.objects.filter(published=True).filter(id__in=instance.posts.all())
        context.update({'posts': queryset})
        self.render_template = instance.template
        return context


class BlogListingPlugin(BlogPluginBase):
    model = BlogListingPluginModel
    name = _('Blog Post Listing')

    def render(self, context, instance, placeholder):
        queryset = Blog.objects.filter(published=True).filter(publication_date__lte=datetime.now())
        error = None
        if instance.tag_filter:
            try:
                queryset = queryset.filter(eval(instance.tag_filter))
            except SyntaxError as err:
                if err.msg:
                    error = err.msg
            except Exception as ex:
                if ex.message:
                    error = ex.message
        # queryset = queryset.filter(Q(tags__name__icontains='www'))
        queryset = queryset.order_by('-publication_date')[
                   instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        context.update({'posts': queryset})
        context.update({'laf': instance.look_and_feel})
        if (error):
            context.update({'error': error})
        self.render_template = instance.template
        return context


class ArticlePluginBase(CMSPluginBase):
    """
    Abstract base class to be used for all Article plugins.
    """

    class Meta:
        abstract = True

    allow_children = False
    # cache = False
    cache = True
    module = _('Article')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False


class ShowArticleDetailPlugin(ArticlePluginBase):
    model = ArticleDetailPlugin
    name = _("Article Details")
    module = _('Article Page Components')
    cache = False

    def render(self, context, instance, placeholder):
        now = timezone.now()
        art = get_object_or_404(Article, pk=instance.article.id)
        if instance.allow_url_to_override_selection:
            q = re.findall('(art)=(\d+)', urlparse.urlparse(context.get('request').get_full_path()).query)
            if q and q[0][0] == 'art':
                pk = int(q[0][1])
                if pk:
                    try:
                        art = get_object_or_404(Article, pk=pk)
                    except:
                        raise Http404("Article not found")
        related_articles = None
        # filter_topics = art.topics.all()
        # if filter_topics and instance.show_related_articles:
        #     filter_main = Article.objects.distinct(id).filter(published=True).filter(topics__in=filter_topics.all())
        #     filter_ex = filter_main.exclude(id=art.id)
        #     # topic_related = filter_ex.order_by('-date')[:3]
        #     topic_related = Article.objects.filter(id__in=filter_ex.all()).order_by('-date')[:3]
        #
        cursor = connection.cursor()
        cursor.execute('''
        select distinct(a.id) as article_id, a.date from spe_blog_article a
	      right outer join spe_blog_article_topics at on at.article_id = a.id
	      where a.published=True
	      and at.topics_id in (select topics_id from spe_blog_article_topics where article_id = %s)
	      and a.id != %s
	      and a.publication_id = %s
	      and a.date <= now()
	      order by date DESC
	      limit 3
	    ''', tuple([art.id, art.id, getPublicationCode(art.publication)]))
        related_article_ids = cursor.fetchall()

        if related_article_ids:
            in_filter = Q()
            ids = []
            for tid, tdate in related_article_ids:
                ids.append(tid)
            in_filter = in_filter | Q(pk__in=ids)
            related_articles = Article.objects.filter(in_filter)
            # related_articles = related_articles.filter(publication__code = art.publication.code)

        request = context.get('request')
        # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
        if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                [y in user_agent.lower() for y in exclude_agents]):
            art.article_hits += 1
            art.article_last_viewed = timezone.now()
            art.save()

            record = ArticleViews()
            record.article = art.id
            record.time = timezone.now()
            record.ip = ip
            vid = context['request'].COOKIES.get('vid', 'not set')
            record.vid = vid
            visitor = get_visitor(context['request'])
            if visitor:
                record.customer_id = visitor.id
            record.save()

        show_paybox = art.show_paybox()
        visitor = None
        if show_paybox:
            # check if this person has a membership or subscription to the publication and set to false instead
            visitor = get_visitor(request)
            if visitor and visitor.is_professional_member() and instance.article.publication.part_of_professional_membership:
                show_paybox = False
            if visitor and visitor.has_subscription(getPublicationCode(instance.article.publication)):
                show_paybox = False
            if visitor and visitor.is_student_member() and instance.article.publication.part_of_student_membership:
                show_paybox = False
        is_readable = art.is_readable()
        if not is_readable:
            if visitor is None:
                visitor = get_visitor(request)
            if visitor and visitor.is_professional_member() and instance.article.publication.part_of_professional_membership:
                is_readable = True
            if visitor and visitor.has_subscription(getPublicationCode(instance.article.publication)):
                is_readable = True
            if visitor and visitor.is_student_member() and instance.article.publication.part_of_student_membership:
                is_readable = True
        is_loggedout = True
        if visitor:
            is_loggedout = False
        context.update({'is_loggedout': is_loggedout})
        context.update({'is_readable': is_readable})
        context.update({'show_paybox': show_paybox})
        context.update({'article': art})
        context.update({'dateNow': now})
        context.update({'topic_articles': related_articles})
        context.update({'show_related_articles': instance.show_related_articles})
        # context.update({'pubcode': self.publication})

        # context.update({'topics_selected': art.topics})
        self.render_template = 'spe_blog/plugins/article_detail.html'
        return context


class ShowArticlesPlugin(ArticlePluginBase):
    model = ArticlesPlugin
    name = _("Selected Articles")
    form = ArticleSelectionForm

    def render(self, context, instance, placeholder):
        queryset = Article.objects.filter(published=True).filter(id__in=instance.articles.all()).order_by(
            instance.order_by)
        context.update({'articles': queryset})
        context.update({'backcol': instance.backcol})
        context.update({'fixedheight': instance.fixedheight})
        context.update({'whitetext': instance.whitetext})
        context.update({'boxwidth': instance.boxwidth})
        context.update({'boxheight': instance.boxheight})
        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        self.render_template = instance.template
        return context


class BriefPluginBase(CMSPluginBase):
    """
    Abstract base class to be used for all Brief plugins.
    """

    class Meta:
        abstract = True

    allow_children = False
    # cache = False
    cache = True
    module = _('Article')
    render_template = 'spe_blog/plugins/brief_interest.html'
    text_enabled = False


class ShowBriefDetailPlugin(BriefPluginBase):
    model = BriefDetailPlugin
    name = _("Brief Details")
    module = _('Article Page Components')
    cache = False

    def render(self, context, instance, placeholder):
        now = timezone.now()
        art = get_object_or_404(Brief, pk=instance.brief.id)
        if instance.allow_url_to_override_selection:
            q = re.findall('(art)=(\d+)', urlparse.urlparse(context.get('request').get_full_path()).query)
            if q and q[0][0] == 'art':
                pk = int(q[0][1])
                if pk:
                    try:
                        art = get_object_or_404(Brief, pk=pk)
                    except:
                        raise Http404("Article not found")
        visitor = None

        request = context.get('request')
        # ip = context['request'].META.get('HTTP_X_REAL_IP', 'internal')
        # ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
        if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                [y in user_agent.lower() for y in exclude_agents]):
            art.article_hits += 1
            art.article_last_viewed = timezone.now()
            art.save()

            record = BriefViews()
            record.article = art.id
            record.time = timezone.now()
            record.ip = ip
            vid = context['request'].COOKIES.get('vid', 'not set')
            record.vid = vid
            visitor = get_visitor(context['request'])
            if visitor:
                record.customer_id = visitor.id
            record.save()

        show_paybox = art.show_paybox()
        if show_paybox:
            # check if this person has a membership or subscription to the publication and set to false instead
            visitor = get_visitor(request)
            if visitor and visitor.is_professional_member() and instance.article.publication.part_of_professional_membership:
                show_paybox = False
            if visitor and visitor.has_subscription(getPublicationCode(instance.brief.publication)):
                show_paybox = False
            if visitor and visitor.is_student_member() and instance.article.publication.part_of_student_membership:
                show_paybox = False
        is_readable = art.is_readable()
        if not is_readable:
            if visitor is None:
                visitor = get_visitor(request)
            if visitor and visitor.is_professional_member() and instance.article.publication.part_of_professional_membership:
                is_readable = True
            if visitor and visitor.has_subscription(getPublicationCode(instance.article.publication)):
                is_readable = True
            if visitor and visitor.is_student_member() and instance.article.publication.part_of_student_membership:
                is_readable = True
        context.update({'is_readable': is_readable})
        context.update({'show_paybox': show_paybox})
        context.update({'article': art})
        context.update({'dateNow': now})
        self.render_template = 'spe_blog/plugins/brief_detail.html'
        return context


class ShowBriefPlugin(BriefPluginBase):
    model = BriefPlugin
    name = _("Selected Briefs ")
    form = BriefSelectionForm

    def render(self, context, instance, placeholder):
        queryset = Brief.objects.filter(published=True).filter(id__in=instance.briefs.all()).order_by(instance.order_by)
        context.update({'articles': queryset})
        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        self.render_template = instance.template
        return context


class ArticleAndBriefPluginBase(CMSPluginBase):
    """
    Abstract base class to be used for all Brief plugins.
    """

    class Meta:
        abstract = True

    allow_children = False
    # cache = False
    cache = True
    module = _('Article')
    render_template = 'spe_blog/plugins/brief_interest.html'
    text_enabled = False


class ShowArticleAndBriefPlugin(ArticleAndBriefPluginBase):
    model = ArticleAndBriefMixPlugin
    name = _("Selected Mixed Articles and Briefs ")
    form = ArticleAndBriefSelectionForm

    def render(self, context, instance, placeholder):
        queryset1 = Article.objects.filter(published=True).filter(id__in=instance.articles.all()).order_by(
            instance.order_by)
        queryset2 = Brief.objects.filter(published=True).filter(id__in=instance.briefs.all()).order_by(
            instance.order_by)
        result_list = sorted(
            chain(queryset1, queryset2),
            key=attrgetter(instance.order_by[1:]),
            reverse=True)
        context.update({'articles': result_list})
        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        context.update({'backcol': instance.backcol})
        context.update({'whitetext': instance.whitetext})
        self.render_template = instance.template
        return context


class TopicsPluginBase(CMSPluginBase):
    """
    Abstract base class to be used for all Topics plugins.
    """

    class Meta:
        abstract = True

    allow_children = False
    cache = False
    # cache = True
    module = _('Article')
    render_template = 'spe_blog/plugins/topics_list.html'
    text_enabled = False


class ShowTopicsListPlugin(TopicsPluginBase):
    model = TopicsListPlugin
    name = _("Topics Listing")
    form = TopicsListSelectionForm
    cache = True

    def render(self, context, instance, placeholder):
        cursor = connection.cursor()
        cursor.execute('''
          select distinct(t.topics_id) as id from spe_blog_topicslistplugin_topics t
          right outer join spe_blog_topicslistplugin p on t.topicslistplugin_id = p.cmsplugin_ptr_id
          right outer join spe_blog_article_topics at on t.topics_id = at.topics_id
          right outer join spe_blog_article a on at.article_id = a.id
          where t.topicslistplugin_id = %s
          and p.cmsplugin_ptr_id is not null
          and at.topics_id is not null
          and a.publication_id = p.publication_id
          and a.published = 1;
        ''', [instance.pk])
        used_topic_ids = cursor.fetchall()

        if used_topic_ids:
            in_filter = Q()
            for tid in used_topic_ids:
                in_filter = in_filter | Q(pk__in=tid)
            topics = instance.topics.filter(in_filter)
        else:
            topics = None

        context.update({'topics': topics})
        context.update({'publication': instance.publication})
        self.render_template = instance.template
        return context


class ShowTopicsListingPlugin(TopicsPluginBase):
    model = TopicsPlugin
    name = _("Topic Details")
    module = _('Article Page Components')

    def render(self, context, instance, placeholder):
        # request = context.get('request')
        art = ''
        now = timezone.now()
        if instance.allow_url_to_override_selection:
            q = re.findall('(topic)=(\d+)', urlparse.urlparse(context.get('request').get_full_path()).query)
            if q and q[0][0] == 'topic':
                pk = int(q[0][1])
                if pk:
                    art = Article.objects.all().filter(published=True).filter(date__lte=datetime.now()).filter(
                        publication=instance.publication).filter(
                        topics__pk=pk).order_by(instance.order_by)[
                          instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
                else:
                    raise Http404("Topic not found")
            else:
                art = Article.objects.all().filter(published=True).filter(date__lte=datetime.now()).filter(
                    publication=instance.publication).filter(
                    topics__pk__in=instance.topics.all()).order_by(instance.order_by).distinct()[
                      instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        else:
            art = Article.objects.all().filter(published=True).filter(date__lte=datetime.now()).filter(
                publication=instance.publication).filter(
                topics__pk__in=instance.topics.all()).order_by(instance.order_by).distinct()[
                  instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        context.update({'articles': art})
        context.update({'dateNow': now})
        self.render_template = instance.template
        return context


class ShowTopicTitlePlugin(TopicsPluginBase):
    model = CMSPlugin
    name = _("Topic Title")

    def render(self, context, instance, placeholder):
        topicid = re.findall('topic=(\d+)', urlparse.urlparse(context.get('request').get_full_path()).query)
        if len(topicid) > 0:
            topicname = Topics.objects.get(pk=topicid[0]).name.upper()
        else:
            topicname = ''

        context.update({'topicname': topicname})
        self.render_template = 'spe_blog/plugins/topic_title_plugin.html'
        return context


class ShowEditorialPlugin(ArticlePluginBase):
    model = EditorialPlugin
    name = _("Selected Editorials")
    form = EditorialSelectionForm

    def render(self, context, instance, placeholder):
        queryset = Editorial.objects.filter(id__in=instance.editorial.all())
        context.update({'editorials': queryset})
        context.update({'link': instance.lnk})
        context.update({'backcol': instance.backcol})
        self.render_template = instance.template
        return context


class ShowBriefListingPlugin(BriefPluginBase):
    model = BriefListingPlugin
    name = _("Brief Listing")
    form = BriefsListSelectionForm

    def render(self, context, instance, placeholder):
        # request = context.get('request')
        cutoff = datetime.now() - timedelta(days=instance.in_last)
        if instance.order_by == "-article_hits":
            qs = Brief.objects.filter(published=True).filter(date__lte=datetime.now(), article_last_viewed__gte=cutoff)
        else:
            qs = Brief.objects.filter(published=True).filter(date__lte=datetime.now())

        if instance.publication:
            qs = qs.filter(publication=instance.publication)

        if instance.categories.all():
            qs = qs.filter(category__in=instance.categories.all())

        if instance.secondary_categories.all():
            qs = qs.filter(secondary_category__in=instance.secondary_categories.all())

        if instance.regions.all():
            qs = qs.filter(region__in=instance.regions.all())

        if instance.print_volume:
            qs = qs.filter(print_volume=instance.print_volume)
        if instance.print_issue:
            qs = qs.filter(print_issue=instance.print_issue)

        qs = qs.order_by(instance.order_by)[
             instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        # NOTE: add other querysets if the publication and discipline is set; need 1 for each combination
        context.update({'articles': qs})
        context.update({'backcol': instance.backcol})
        context.update({'whitetext': instance.whitetext})
        context.update({'boxtitle': instance.boxtitle})
        if instance.publication:
            context.update({'pubcode': getPublicationCode(instance.publication)})
        else:
            context.update({'pubcode': ""})
        context.update({'isbrief': True})
        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        self.render_template = instance.template
        return context


class ShowArticlesListingPlugin(ArticlePluginBase):
    model = ArticlesListingPlugin
    name = _("Articles Listing")
    form = ArticlesListSelectionForm
    cache = False

    def render(self, context, instance, placeholder):
        request = context.get('request')
        visitor = get_visitor(request)

        # NOTE: change this to be set in the context globally and stored server side
        ducode = None
        dcode = None
        if instance.personalized:
            if visitor:
                # The Member is Logged In & Has Discipline
                if visitor.primary_discipline:
                    if visitor.primary_discipline.active:
                        # Member - Primary Discipline Available
                        ducode = visitor.primary_discipline
        if instance.discipline:
            dcode = instance.discipline.code
        context.update({'ducode': ducode, 'dcode': dcode})
        cutoff_1 = datetime.now() - timedelta(days=instance.in_last)
        cutoff_2 = datetime.now() - timedelta(days=instance.published_in_last)
        # if instance.this_month:
        #     cutoff2 = datetime.now() - timedelta(days=int(datetime.now().strftime("%d")))
        #     qs = Article.objects.filter(published=True).filter(date__lte=datetime.now(), date__gte=cutoff2, article_last_viewed__gte=cutoff)
        # else:
        #     qs = Article.objects.filter(published=True).filter(date__lte=datetime.now(), article_last_viewed__gte=cutoff)
        if instance.order_by == "-article_hits":
            qs = Article.objects.filter(published=True).filter(date__lte=datetime.now(),
                                                               article_last_viewed__gte=cutoff_1, date__gte=cutoff_2)
        else:
            qs = Article.objects.filter(published=True).filter(date__lte=datetime.now())

        if instance.publication:
            qs = qs.filter(publication=instance.publication)

        if instance.categories.all():
            qs = qs.filter(category__in=instance.categories.all())

        if instance.secondary_categories.all():
            qs = qs.filter(secondary_category__in=instance.secondary_categories.all())

        if instance.print_volume:
            qs = qs.filter(print_volume=instance.print_volume)
        if instance.print_issue:
            qs = qs.filter(print_issue=instance.print_issue)

        if ducode:
            qs = qs.filter(disciplines=ducode).order_by(instance.order_by)[
                 instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        elif dcode:
            qs = qs.filter(disciplines=dcode).order_by(instance.order_by)[
                 instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        else:
            qs = qs.order_by(instance.order_by)[instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        # NOTE: add other querysets if the publication and discipline is set; need 1 for each combination
        context.update({'articles': qs})
        context.update({'backcol': instance.backcol})
        context.update({'backtransp': instance.backtransp})
        context.update({'fixedheight': instance.fixedheight})
        context.update({'whitetext': instance.whitetext})
        context.update({'boxwidth': instance.boxwidth})
        context.update({'boxheight': instance.boxheight})
        context.update({'boxtitle': instance.boxtitle})
        context.update({'pubcode': getPublicationCode(instance.publication)})

        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        self.render_template = instance.template
        return context


class ShowIssuesByPublicationPlugin(CMSPluginBase):
    model = IssuesByPublicationPlugin
    allow_children = False
    # cache = False
    cache = True
    module = _('Publications')
    name = _('Issues by Publication Listing')
    text_enabled = False
    render_template = 'spe_blog/plugins/issue_channel.html'

    # render_plugin = False

    def render(self, context, instance, placeholder):
        queryset = Issue.objects.filter(publication=instance.publication).filter(active=True).filter(
            date__lte=datetime.now()).order_by('-date')[
                   instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
        context.update({'publication': instance.publication})
        context.update({'issues': queryset})
        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        context.update({'show_subscribe_url': instance.publication.subscription_url})
        self.render_template = instance.template
        return context


class ShowBreadCrumbPlugin(CMSPluginBase):
    model = BreadCrumbPlugin
    allow_children = False
    cache = False
    module = _('Publications')
    name = _('Bread Crumb')
    text_enabled = False
    render_template = 'spe_blog/plugins/bread_crumb.html'

    def render(self, context, instance, placeholder):
        context.update({'title': instance.title})
        return context


class ShowIssuesByYearPlugin(CMSPluginBase):
    model = IssuesByYearPlugin
    allow_children = False
    # cache = False
    cache = True
    module = _('Publications')
    name = _('Issues by Year Listing')
    text_enabled = False
    render_template = 'spe_blog/plugins/issues_by_year.html'

    def render(self, context, instance, placeholder):
        issues = Issue.objects.filter(publication=instance.publication).order_by('-date')
        context.update({'issues': issues})
        return context


class ShowTagsDetailPlugin(CMSPluginBase):
    model = TagsDetailPlugin
    allow_children = False
    # cache = False
    cache = False
    module = _('Article Page Components')
    name = _('Tags Details')
    text_enabled = False
    render_template = 'spe_blog/plugins/image_left.html'

    def render(self, context, instance, placeholder):
        art = ''
        now = timezone.now()
        q = re.findall('(tag)=(\d+)', urlparse.urlparse(context.get('request').get_full_path()).query)
        if q and q[0][0] == 'tag':
            pk = int(q[0][1])
            if pk:
                art = Article.objects.all().filter(published=True).filter(date__lte=datetime.now()).filter(
                    publication=instance.publication).filter(
                    tags__pk=pk).order_by(instance.order_by)[
                      instance.starting_with - 1:instance.starting_with + instance.cnt - 1]
            else:
                raise Http404("Tag not found")
        context.update({'articles': art})
        context.update({'dateNow': now})
        self.render_template = instance.template
        return context


class ShowTagTitlePlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Tag Title")
    allow_children = False
    # cache = False
    cache = True
    module = _('Article')
    text_enabled = False
    render_template = 'spe_blog/plugins/topic_title_plugin.html'

    def render(self, context, instance, placeholder):
        tag_id = re.findall('tag=(\d+)', urlparse.urlparse(context.get('request').get_full_path()).query)
        if len(tag_id) > 0:
            topicname = Tag.objects.get(pk=tag_id[0]).name.upper()
        else:
            topicname = ''

        context.update({'topicname': topicname})
        return context


class ShowIssueCoverPlugin(CMSPluginBase):
    model = IssueCoverPlugin
    allow_children = False
    # cache = False
    cache = True
    module = _('Publications')
    name = _('Issue Cover Plugin')
    text_enabled = False
    render_template = 'spe_blog/plugins/on_the_cover.html'

    def render(self, context, instance, placeholder):
        queryset = Issue.objects.get(pk=instance.issue.id)
        context.update({'issue': queryset})
        # context.update({'issues': issue})
        if instance.all_url:
            context.update({'show_all_url': instance.all_url.get_absolute_url()})
            context.update({'show_all_text': instance.all_text})
        context.update({'show_subscribe_url': instance.publication.subscription_url})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(BlogPlugin)
plugin_pool.register_plugin(BlogListingPlugin)
plugin_pool.register_plugin(BlogDetailPlugin)
plugin_pool.register_plugin(ShowArticleDetailPlugin)
plugin_pool.register_plugin(ShowArticlesPlugin)
plugin_pool.register_plugin(ShowArticlesListingPlugin)
plugin_pool.register_plugin(ShowBriefDetailPlugin)
plugin_pool.register_plugin(ShowBriefPlugin)
plugin_pool.register_plugin(ShowBriefListingPlugin)
plugin_pool.register_plugin(ShowArticleAndBriefPlugin)
plugin_pool.register_plugin(ShowTagsDetailPlugin)
plugin_pool.register_plugin(ShowIssuesByPublicationPlugin)
plugin_pool.register_plugin(ShowIssueCoverPlugin)
# plugin_pool.register_plugin(ShowBreadCrumbPlugin)
plugin_pool.register_plugin(ShowIssuesByYearPlugin)
plugin_pool.register_plugin(ShowTopicsListPlugin)
plugin_pool.register_plugin(ShowTopicsListingPlugin)
plugin_pool.register_plugin(ShowTopicTitlePlugin)
plugin_pool.register_plugin(ShowTagTitlePlugin)
