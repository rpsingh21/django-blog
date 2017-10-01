from django.conf.urls import url

from .views import (
	instance_comments,
	)

urlpatterns = [
	url(r'^(?P<object_id>\d+)/$',instance_comments,name='comments'),
]
