from django.conf.urls import url

from . import views

# app_name='helloworld'
urlpatterns = [
    # ex: /helloworld/
    url(r'^$', views.index, name='index'),
    # ex: /helloworld/5/
    # url(r'^(?P<message_id>[0-9]+)/$', views.detail, name='detail'),
]
