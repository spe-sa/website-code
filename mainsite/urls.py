# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'/ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # ran into a problem where the ckeditor is not at the root
    # ex: /en/admin/spe_blog/article/add/ckeditor/upload/?CKEditor=id_introduction&CKEd...
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^staff/articles/', include('spe_blog.urls_internal')),
    url(r'^spe_links/', include('spe_links.urls')),
    #url(r'^contact/', include('spe_contact.urls')),
    url(r'^localhost/login/do', 'mainsite.views.do_login', name='dologin'),
    url(r'^localhost/login/show', 'mainsite.views.login_show', name='showlogin'),
    url(r'^localhost/logout/', 'mainsite.views.logout', name='logout'),
    url(r'^localhost/login/', 'mainsite.views.login', name='login'),
    url(r'^polls/', include('spe_polls.urls', namespace='polls')),
    url(r'^forms/', include('djangocms_forms.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^preferences/', include('spe_preferences.urls')),

    url(r'^admin/', include(admin.site.urls)),  # NOQA
    # ex: /ogf/  -> /ogf/ogf-main-page/
    url(r'^ogf/$', RedirectView.as_view(url='ogf-main-page/', permanent=True), name='ogf-main-page'),
    url(r'^twa/$', RedirectView.as_view(url='twa-main-page/', permanent=True), name='twa-main-page'),
    url(r'^ogf/ogf-main-page/googleaa5ff496c6812444.html', 'mainsite.views.register_ogf', name='google-registration-ogf'),
    url(r'^', include('cms.urls')),
)



# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^en/media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),) \
                  + staticfiles_urlpatterns() + urlpatterns  # NOQA
