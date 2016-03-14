from django.conf.urls import url

from . import views

# app_name='spe_blog'
urlpatterns = [
    # ex: /articles/
    url(r'^$', views.index, name='index'),
    # ex: /articles/publications/(?P<publication_code>)/issues
    url(r'^publications/(?P<publication_code>[0-9A-Za-z-_./]+)/issues/$', views.issue, name='issue'),
    # ex: /articles/month/slug
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]
