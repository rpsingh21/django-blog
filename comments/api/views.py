from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.mixins import (
	UpdateModelMixin,
	DestroyModelMixin,
	)

from comments.models import Comments
from posts.models import Posts

from .serializers import (
	PostCommentsSerializer,
	PostCommentsCreateSerializer,
	CommentsCreateSerializer,
	)

class CommentsListAPIView(ListAPIView):
	queryset = Comments.objects.all()
	serializer_class = PostCommentsSerializer

class InstanceCommentsListAPIView(ListAPIView):
	serializer_class = PostCommentsSerializer
	def get_queryset(self):
		object_id = self.kwargs['object_id']
		return Comments.objects.all().filter(object_id=object_id).distinct()

class CommentCreateAPIView(CreateAPIView):
	queryset=Comments.objects.all()
	serializer_class = PostCommentsCreateSerializer

	def get_serializer_context(self):
		context = super(CommentCreateAPIView, self).get_serializer_context()
		context['user'] = self.request.user
		return context

class CommentEditOrDeleteAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
	serializer_class=CommentsCreateSerializer
	queryset=Comments.objects.filter(id__gte=0)

	def put (self,request,*arg,**kwarg):
		return self.update(request,*arg,**kwarg)

	def delete (self,request,*arg,**kwarg):
		return self.destroy(request, *arg, **kwarg)

