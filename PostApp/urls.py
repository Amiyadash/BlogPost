from django.conf.urls import url
from PostApp.views import *

urlpatterns = [
    url(r'^$',post_list),
    url(r'^create$',post_create),
    url(r'^(?P<id>\d+)/$',post_details,name='detail'),
    url(r'^delete$',post_delete),
    url(r'^(?P<id>\d+)/edit$',post_update,name='update'),
]