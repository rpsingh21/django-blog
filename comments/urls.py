from django.urls import re_path

from .views import (
    instance_comments,
    reply_form,
    comment_delete,
    comment_activity,
    )

urlpatterns = [
    re_path(r'^(?P<object_id>\d+)/(?P<slug>[\w-]+)/$', instance_comments, name='comments'),
    re_path(r'^(?P<slug>[\w-]+)/(?P<parent_id>\d+)/$', reply_form, name='reply_form'),
    re_path(r'^delete/(?P<pk>\d+)/$', comment_delete, name="delete"),
    re_path(r'^activity/(?P<id>\d+)/(?P<activity_type>[\w-]+)/$', comment_activity, name="comment_activity"),
]
