from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/
    # url(r'^$', views.index, name='index'),
    # ex: /api/validation/url/
    url(r'^validation/url/$', views.UrlValidation.as_view(), name='validation-url'),
    url(r'^filer/lookup/$', views.FilerLookup.as_view(), name='old-filer-lookup'),
]
