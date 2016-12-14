from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /briefs/regional/
    url(r'^regional/$', views.brief_regional, name='brief_regional'),
    # # ex: /briefs/?
    # url(r'^/(?P<brief_id>[0-9]+)/$', views.brief_detail, name='brief_detail'),
]
