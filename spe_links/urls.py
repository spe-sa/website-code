from django.conf.urls import url

from . import views

app_name = 'spe_links'
urlpatterns = [
    # ex: /spe_links/
    url(r'^$', views.index, name='index'),
    # ex: /spe_links/5/
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
]
