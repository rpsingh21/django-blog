from django.conf.urls import url

from .views import (
	ActivitysListAPIView,
	ActivitysCreateAPIView,
	ActivitysRetrieveUpdateDestroyAPIView,
	)

urlpatterns = [
	url(r'^$',ActivitysListAPIView.as_view(),name='activitys'),
	url(r'^create/$',ActivitysCreateAPIView.as_view(),name='create'),
	url(r'^edit/(?P<pk>\d+)/$',ActivitysRetrieveUpdateDestroyAPIView.as_view(),name='update'),
]
