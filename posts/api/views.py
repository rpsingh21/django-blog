from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from posts.models import Posts

from .serializers import (
	PostSerializer,
	)

class PostListAPIView(ListAPIView):
	queryset = Posts.objects.all()
	serializer_class = PostSerializer