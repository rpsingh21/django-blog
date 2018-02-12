from django.conf.urls import url

from .views import (
    instance_comments,
    reply_form,
    comment_delete,
    comment_activity,
    )

urlpatterns = [
    url(r'^(?P<object_id>\d+)/(?P<slug>[\w-]+)/$', instance_comments, name='comments'),
    url(r'^(?P<slug>[\w-]+)/(?P<parent_id>\d+)/$', reply_form, name='reply_form'),
    url(r'^delete/(?P<pk>\d+)/$', comment_delete, name="delete"),
    url(r'^activity/(?P<id>\d+)/(?P<activity_type>[\w-]+)/$', comment_activity, name="comment_activity"),
]
