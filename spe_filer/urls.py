from django.conf.urls import url

from . import views

app_name = 'spe_filer'
urlpatterns = [
    # ex: /spe_filer/
    url(r'^$', views.browse, name='filebrowse'),
    url(r'^list/json/', views.browse_json, name='jsonlist'),
    # ex: /spe_filer/upload/
    url(r'^add_dir/', views.addDirectory, name='adddirectory'),
    # ex: /spe_filer/upload/
    url(r'^upload/', views.upload, name='fileupload'),
    # ex: /spe_filer/fileid/
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
]
