from django.conf.urls import url

from . import views

# app_name='spe_preferences'
urlpatterns = [
    url(r'^hi$', views.hello_world, name='hello_world'),
    url(r'^set/?$', views.prefs_new, name='prefs_new'),
    # NOTE: we should have no publicly defined views; moved to urls_internal
    # SEE: urls_internal.py
    # # ex: /articles/
    # url(r'^staff/$', views.article_index, name='article_index'),
    # # ex: /articles/briefs/
    # url(r'^staff/briefs/$', views.brief_index, name='brief_index'),
    # # ex: /articles/publications/(?P<publication_code>)/issues
    # url(r'^staff/publications/(?P<publication_code>[0-9A-Za-z-_./]+)/issues/$', views.issue, name='issue'),
    # # ex: /articles/article/?
    # url(r'^staff/article/(?P<article_id>[0-9]+)/$', views.article_detail, name='article_detail'),
    # # ex: /articles/brief/?
    # url(r'^staff/brief/(?P<brief_id>[0-9]+)/$', views.brief_detail, name='brief_detail'),
]
