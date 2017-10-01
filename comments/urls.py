from django.conf.urls import url

from .views import (
	instance_comments,
	reply_form,
	comment_delete,
	)

urlpatterns = [
	url(r'^(?P<object_id>\d+)/$',instance_comments,name='comments'),
	url(r'^(?P<slug>[\w-]+)/(?P<parent_id>\d+)/$',reply_form,name='reply_form'),
	url(r'^delete/(?P<pk>\d+)/$', comment_delete,name="delete"),
]
