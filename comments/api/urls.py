from django.conf.urls import url

from .views import (
    CommentsListAPIView,
    InstanceCommentsListAPIView,
    CommentCreateAPIView,
    CommentEditOrDeleteAPIView,
    CommentDestroyAPIView,
    )
urlpatterns = [
    url(r'^$', CommentsListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<object_id>\d+)/$', InstanceCommentsListAPIView.as_view(), name='post-commments'),
    url(r'^edit/(?P<pk>\d+)/$', CommentEditOrDeleteAPIView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', CommentDestroyAPIView.as_view(), name="delete"),
]
