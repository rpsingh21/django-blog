from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)

from activitys.models import Activitys
from account.api.serializers import UserDetailSerializer

User=get_user_model()

class ActivitysDetailSerializer(ModelSerializer):
	class Meta:
		model=Activitys
		fields=[
			'id',
			'user',
			'activity_type',
			'date',
			'content_type',
			'object_id',
		]

class ActivitysUpdateOrDeleteSerializer(ModelSerializer):
	class Meta:
		model=Activitys
		fields=[
			'activity_type',
		]

class ActivitysCreateSerializer(ModelSerializer):
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model=Activitys
		fields=[
			'user',
			'activity_type',
			'content_type',
			'object_id',
		]

	def validate(self,data):
		content_type = data.get("content_type");
		content_qs = ContentType.objects.filter(model=content_type)
		if not content_qs.exists() or content_qs.count() != 1:
			raise ValidationError("This is not valid content type")

		object_id = data.get("object_id")
		obj_model = content_qs.first().model_class()
		obj_qs = obj_model.objects.filter(id=object_id)
		if not obj_qs.exists() or obj_qs.count() !=1:
			raise ValidationError("Not valid Object Id")

		activity_type = data.get("activity_type")
		if not activity_type in ['L',"F","U","D"]:
			raise ValidationError("Not valid activity")

		return data

	def create(self,data):
		content_type = data.get("content_type")
		object_id = data.get("object_id")
		activity_type = data.get("activity_type")
		user = self.context['user']

		activity_qs = Activitys.objects.filter(content_type=content_type,user=user,object_id=object_id)
		if activity_qs.exists():
			raise ValidationError("Not valid opretion ")

		activity = Activitys.objects.create(content_type=content_type,object_id=object_id,user=user,activity_type=activity_type)
		return activity
