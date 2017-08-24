# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

# from cms.sitemaps import CMSSitemap
from djangocms_page_sitemap.sitemap import ExtendedSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView


# Dashboard

from dashing.utils import router
from dashboard.widgets import ArticleCountWidget, BriefCountWidget, PromotionCountWidget, TopFiveArticlesWidget, TopTwentyArticlesWidget, TopFiveBriefsWidget, TopTwentyBriefsWidget
router.register(ArticleCountWidget, 'article_count')
router.register(BriefCountWidget, 'brief_count')
router.register(PromotionCountWidget, 'promotion_count')
router.register(TopFiveArticlesWidget, 'top_5_articles')
router.register(TopTwentyArticlesWidget, 'top_20_articles')
router.register(TopFiveBriefsWidget, 'top_5_briefs')
router.register(TopTwentyBriefsWidget, 'top_20_briefs')


# # Model Reports
#
# from model_report import report
# report.autodiscover()


# TastyPIE APIs

from tastypie.api import Api
from spe_promotions.api import MembershipPromotionsClicksResource, PromotionsEventClicksResource, SimpleEventPromotionResource

api = Api(api_name='reports')
api.register(MembershipPromotionsClicksResource())
api.register(PromotionsEventClicksResource())
api.register(SimpleEventPromotionResource())

# Specialized Sitemaps

from django.contrib.sitemaps.views import sitemap

from spe_blog.sitemap import AllArticlesSitemap, AllBriefsSitemap

sitemaps = {
    'articles': AllArticlesSitemap,
    'briefs': AllBriefsSitemap,
}

# Admin

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # url(r'/ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^iptcnet/2014/', 'mainsite.views.status_code_410', ),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
    # ran into a problem where the ckeditor is not at the root
    # ex: /en/admin/spe_blog/article/add/ckeditor/upload/?CKEditor=id_introduction&CKEd...
    # url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
    #     {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': ExtendedSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    # NOTE: for more specific staff stuff put first; blog will catch anything else /staff.
    # ex url(r'^staff/filer/', include('spe_filer.urls_internal')),
    url(r'^staff/dashboard/', include(router.urls)),

    url(r'^staff/promotions/export_statistics/', 'spe_promotions.views.export_excel', ),
    url(r'^staff/promotions/export_summary/', 'spe_promotions.views.export_summary_excel', ),
    url(r'^staff/promotions/export_details/', 'spe_promotions.views.export_detail_excel', ),
    url(r'^staff/promotions/timeline/', 'spe_promotions.views.promotion_timeline', ),
    url(r'^staff/promotions/discipline/', 'spe_promotions.views.promotion_by_discipline', ),
    url(r'^staff/promotions/region/', 'spe_promotions.views.promotion_by_region', ),
    url(r'^staff/promotions/event_type/', 'spe_promotions.views.promotion_by_event_type', ),
    url(r'^staff/promotions/search/', 'spe_promotions.views.filter_simple_promotions', ),
    url(r'^staff/membership/search/', 'spe_promotions.views.filter_simple_membership', ),
    url(r'^staff/articles/export_details/', 'spe_blog.views.export_article_detail_excel', ),
    url(r'^staff/briefs/export_details/', 'spe_blog.views.export_brief_detail_excel', ),
    url(r'^staff/articles/export_article_disciplines/', 'spe_blog.views.export_article_disciplines_excel', ),
    url(r'^staff/articlesandbriefs/sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # url(r'^staff/report/', include('model_report.urls'), ),
    url(r'^staff/api/', include(api.urls)),
    url(r'^staff/ads/', 'mainsite.views.send_email', name='submit_ad'),
#    url(r'^staff/schedules/', include('spe_event_schedules.urls')),
    url(r'^staff/', include('spe_blog.urls_internal')),
    url(r'^spe_links/', include('spe_links.urls')),
    url(r'^briefs/', include('spe_blog.urls_brief')),
    #url(r'^contact/', include('spe_contact.urls')),
    url(r'^localhost/login/do', 'mainsite.views.do_login', name='dologin'),
    url(r'^localhost/login/show', 'mainsite.views.login_show', name='showlogin'),
    url(r'^localhost/logout/', 'mainsite.views.logout', name='logout'),
    url(r'^localhost/login/', 'mainsite.views.login', name='login'),
    # url(r'^test/gtm/', 'mainsite.views.test_gtm', name='test_gtm'),
    url(r'^polls/', include('spe_polls.urls', namespace='polls')),
    url(r'^forms/', include('djangocms_forms.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^preferences/', include('spe_preferences.urls')),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    # ex: /ogf/  -> /ogf/ogf-main-page/
    url(r'^ogf/$', RedirectView.as_view(url='ogf-main-page/', permanent=True), name='ogf-main-page'),
    url(r'^twa/$', RedirectView.as_view(url='twa-main-page/', permanent=True), name='twa-main-page'),
    url(r'^jpt/$', RedirectView.as_view(url='jpt-main-page/', permanent=True), name='jpt-main-page'),
    url(r'^ogf/ogf-main-page/googleaa5ff496c6812444.html', 'mainsite.views.register_ogf', name='google-registration-ogf'),

    url(r'^favicon\.ico', 'mainsite.views.status_code_418', name='status_code_418'),

    # url(r'^test/sc200', 'mainsite.views.status_code_200', name='status_code_200'),
    # url(r'^test/sc301', 'mainsite.views.status_code_301', name='status_code_301'),
    # url(r'^test/sc404', 'mainsite.views.status_code_404', name='status_code_404'),
    # url(r'^test/sc410', 'mainsite.views.status_code_410', name='status_code_410'),
    # url(r'^test/sc418', 'mainsite.views.status_code_418', name='status_code_418'),
    # url(r'^test/sc500', 'mainsite.views.status_code_500', name='status_code_500'),
    # url(r'^dashboard/', include(router.urls)),
    # url(r'^stats/$', 'dashboard.views.url_redirect', name="url-redirect"),
    url(r'^promotion/event/(?P<index>\d+)/$', 'spe_promotions.views.event_select',),
    url(r'^promotion/no_discipline/(?P<index>\d+)/$', 'spe_promotions.views.no_discipline',),
    url(r'^promotion/no_region/(?P<index>\d+)/$', 'spe_promotions.views.no_region', ),
    url(r'^promotion/non_member/(?P<index>\d+)/$', 'spe_promotions.views.non_member', ),
    url(r'^promotion/not_logged_in/(?P<index>\d+)/$', 'spe_promotions.views.not_logged_in', ),
    url(r'^promotion/membership/(?P<index>\d+)/$', 'spe_promotions.views.membership_select', ),
    url(r'^promotion/membership/no_discipline/(?P<index>\d+)/$', 'spe_promotions.views.membership_no_discipline', ),
    url(r'^promotion/membership/no_region/(?P<index>\d+)/$', 'spe_promotions.views.membership_no_region', ),
    url(r'^events/(?P<event_id>\d+)/export/', 'spe_events.views.export', name="event_ics_export"),
    url(r'^agenda/(?P<agenda_id>\d+)/export/', 'spe_custom_agenda.views.export', name="agenda_ics_export"),
    # url(r'^stats/', include('statsy.urls')),
    url(r'^api/', include('spe_api.urls')),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^en/media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),) \
                  + staticfiles_urlpatterns() + urlpatterns  # NOQA
