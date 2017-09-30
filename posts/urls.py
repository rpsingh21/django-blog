from django.conf.urls import url

from .views import (
	post_list,
	post_detail,
	post_create,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$',post_list,name='list'),
	url(r'details/(?P<slug>[\w-]+)/$',post_detail,name='detail'),
	url(r'create/$',post_create,name='create'),
	url(r'update/(?P<slug>[\w-]+)/$',post_update,name='update'),
	url(r'delete/(?P<slug>[\w-]+)/$',post_delete,name='delete'),
]
