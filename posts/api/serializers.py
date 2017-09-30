from django.contrib.auth import get_user_model

from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)

from posts.models import Posts
from account.api.serializers import UserDetailSerializer

class PostSerializer(ModelSerializer):
	user = UserDetailSerializer()
	class Meta:
		model=Posts
		fields="__all__"

class PostDetailsSerializer(ModelSerializer):
	user = UserDetailSerializer()
	class Meta:
		model=Posts
		fields="__all__"
		