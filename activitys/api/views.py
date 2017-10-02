from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveUpdateDestroyAPIView,
	)

from rest_framework.mixins import (
	UpdateModelMixin,
	DestroyModelMixin,
	)

from activitys.models import Activitys

from .serializers import (
	ActivitysDetailSerializer,
	ActivitysCreateSerializer,
	ActivitysUpdateOrDeleteSerializer,
	)

class ActivitysListAPIView(ListAPIView):
	queryset = Activitys.objects.all()
	serializer_class = ActivitysDetailSerializer

class ActivitysCreateAPIView(CreateAPIView):
	queryset = Activitys.objects.all()
	serializer_class = ActivitysCreateSerializer

	def get_serializer_context(self):
		context = super(ActivitysCreateAPIView, self).get_serializer_context()
		context['user'] = self.request.user
		return context

class ActivitysRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Activitys.objects.all()
	serializer_class = ActivitysUpdateOrDeleteSerializer
	lookup_field = "pk"