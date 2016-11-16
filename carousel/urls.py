from django.conf.urls import url

from . import views

# carousel should be tagged with each component id when it creates the links; the related info can be looked up by id
urlpatterns = [
    url(r'^clicked/(?P<component_id>\w+)/$', views.clicked, name='clicked'),
    url(r'^viewed/(?P<component_id>\w+)/$', views.viewed, name='viewed'),
]
