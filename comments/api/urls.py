from django.urls import re_path

from .views import (
    CommentsListAPIView,
    InstanceCommentsListAPIView,
    CommentCreateAPIView,
    CommentEditOrDeleteAPIView,
    CommentDestroyAPIView,
    )
urlpatterns = [
    re_path(r'^$', CommentsListAPIView.as_view(), name='list'),
    re_path(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<object_id>\d+)/$', InstanceCommentsListAPIView.as_view(), name='post-commments'),
    re_path(r'^edit/(?P<pk>\d+)/$', CommentEditOrDeleteAPIView.as_view(), name="update"),
    re_path(r'^delete/(?P<pk>\d+)/$', CommentDestroyAPIView.as_view(), name="delete"),
]
