from django.conf.urls import url

from . import views

# app_name='spe_blog'
urlpatterns = [
    # ex: /staff/
    url(r'^$', views.staff_index, name='staff_index'),
    # ex: /staff/articles/
    url(r'^articles/$', views.article_index, name='article_index'),
    # ex: /staff/articles/briefs/
    url(r'^briefs/$', views.brief_index, name='brief_index'),
    # ex: /staff/articles/publications/(?P<publication_code>)/issues
    url(r'^publications/(?P<publication_code>[0-9A-Za-z-_./]+)/issues/$', views.issue, name='issue'),
    # ex: /staff/articles/article/?
    url(r'^articles/article/(?P<article_id>[0-9]+)/$', views.article_detail, name='article_detail'),
    # ex: /staff/articles/brief/?
    url(r'^briefs/brief/(?P<brief_id>[0-9]+)/$', views.brief_detail, name='brief_detail'),
    # used for i2k article data crawling
    url(r'^crawler/', views.article_links, name='article_links'),
]
