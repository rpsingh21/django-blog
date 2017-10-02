from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError,
	SlugField,
	IntegerField
	)

from comments.models import Comments
from account.api.serializers import UserDetailSerializer

class PostCommentsSerializer(ModelSerializer):
	user 		= UserDetailSerializer()
	replies 	= SerializerMethodField()
	reply_count = SerializerMethodField()
	class Meta:
		model=Comments
		fields=[
			'user',
			'id',
			'parent',
			'content',
			'timestamp',
			'replies',
			'reply_count',
		]	

	def get_replies(self,obj):
		return PostCommentsSerializer(obj.childer(),many=True).data

	def get_reply_count(self,obj):
		return obj.childer().count()

class PostCommentsCreateSerializer(ModelSerializer):
	user 		= UserDetailSerializer(read_only=True)
	type 		= CharField(required=False, write_only=True)
	slug 		= SlugField(write_only=True)
	parent_id 	= IntegerField(required=False)
	class Meta:
		model=Comments
		fields=[
			'id',
			'user',
			'type',
			'slug',
			'parent_id',
			'content',
			'timestamp'
		]

	def validate(self, data):
		model_type 	= data.get("type","posts")
		model_qs = ContentType.objects.filter(model=model_type)
		if not model_qs.exists() or model_qs.count() != 1:
			raise ValidationError("This is not valid content type")

		someModel = model_qs.first().model_class()
		slug 	= data.get("slug")
		obj_qs 	= someModel.objects.filter(slug=slug)
		if not obj_qs.exists() or obj_qs.count() !=1:
			raise ValidationError("This is not slug for comments")

		parent_id = data.get("parent_id")
		if parent_id:
			parent_qs = Comments.objects.filter(id=parent_id)
			if not parent_qs.exists() or parent_qs.count() != 1:
				raise ValidationError("This is not valid parent")
				
		return data

	def create(self, validated_data):
		content =validated_data.get("content")
		model_type =validated_data.get("type","posts")
		slug = validated_data.get("slug")
		parent_id = validated_data.get("parent_id")
		parent_obj = None
		if parent_id:
			parent_obj = Comments.objects.filter(id=parent_id).first()
		user = self.context['user']
		comment = Comments.objects.create_by_model_type(model_type,slug,content,user,parent_obj=parent_obj)
		return comment

class CommentsCreateSerializer(ModelSerializer):
	class Meta:
		model = Comments
		fields = [
			'content'
		]