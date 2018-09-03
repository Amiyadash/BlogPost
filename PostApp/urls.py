from django.conf.urls import url
from PostApp.views import *

urlpatterns = [
    url(r'^$',post_list,name='list'),
    url(r'^create$',post_create),
    url(r'^(?P<id>\d+)/$',post_details,name='detail'),
    url(r'^(?P<id>\d+)/delete/$',post_delete,name='delete'),
    url(r'^(?P<id>\d+)/edit$',post_update,name='update'),
]