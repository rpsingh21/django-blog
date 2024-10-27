from django.urls import re_path

from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    )

urlpatterns = [
    re_path(r'^$', post_list, name='list'),
    re_path(r'details/(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'create/$', post_create, name='create'),
    re_path(r'update/(?P<slug>[\w-]+)/$', post_update, name='update'),
    re_path(r'delete/(?P<slug>[\w-]+)/$', post_delete, name='delete'),
]
