from django.conf.urls import url
from . import views


# app_name='spe_preferences'
urlpatterns = [
    url(r'^myip/?$', views.myip, name="myip"),
    #url(r'^comm_prefs/?$', views.comm_prefs, name='comm'),
    url(r'^co(?:ntact|mm)(?:(?:unication)?s?_pref(?:erence?)?s?)?/?$', views.contact_prefs, name='contact'),
    url(r'^contact_prefs/?$', views.contact_prefs, name='contact'),

    url(r'^who/(?P<constituent_id_provided>ci:[0-9a-zA-Z]+)?(?P<email_address_provided>ea:[0-9a-zA-Z_.-]+@[0-9a-zA-Z_.-]+\.[0-9a-zA-Z]+)?$', views.quick_find_user, name='who'),
    url(r'^allow/(?P<preference_code>[a-z0-9A-Z]+):(?P<yes_or_no>[YyEeSsNnOoTtRrUuFfAaLl10]+)$', views.allow_communication_for, name='allow'),

    url(r'^interests/?$', views.additional_prefs_search, name='add_prefs_search'),
    url(r'^interests/save/$', views.additional_prefs_insert, name='add_prefs_insert'),
]
