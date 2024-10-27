from django.urls import re_path

from .views import (
    ActivitysListAPIView,
    ActivitysCreateAPIView,
    ActivitysRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    re_path(r'^$', ActivitysListAPIView.as_view(), name='activitys'),
    re_path(r'^create/$', ActivitysCreateAPIView.as_view(), name='create'),
    re_path(r'^edit/(?P<pk>\d+)/$', ActivitysRetrieveUpdateDestroyAPIView.as_view(), name='update'),
]
