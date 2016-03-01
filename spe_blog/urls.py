from django.conf.urls import url

from . import views

# app_name='spe_blog'
urlpatterns = [
    # ex: /spe_blog/
    url(r'^$', views.index, name='index'),
    # ex: /spe_blog/article/5/
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]
