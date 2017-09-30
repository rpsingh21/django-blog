from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from posts.models import Posts, Activitys
# Create your models here.

# 	COMMENT MANAGER 
class CommentsManerger(models.Manager):
	def all(self):
		commnets=super(CommentsManerger,self).filter(parent=None)
		return commnets

	def filter_by_instance(self,instance):
		content_type=ContentType.objects.get_for_model(instance.__calss__)
		object_id=instance.object_id
		commnets=super(CommentsManerger,self).filter(content_type=content_type,object_id=objects_id).filter(parent=None)
		return commnets

	def create_by_model_type(self, model_type, slug, content, user, parent_obj=None):
		model_qs = ContentType.objects.filter(model=model_type)
		if model_qs.exists():
			SomeModel = model_qs.first().model_class()
			obj_qs = SomeModel.objects.filter(slug=slug)
			if obj_qs.exists() and obj_qs.count() == 1:
				instance = self.model()
				instance.content = content
				instance.user = user
				instance.content_type = model_qs.first()
				instance.object_id = obj_qs.first().id
				if parent_obj:
					instance.parent = parent_obj
				instance.save()
				return instance
		return None


# model for commnets 
class Comments(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	parent = models.ForeignKey("self",blank=True,null=True)
	content = models.TextField()

	# genric foreignkey fields
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type','object_id')

	activity = GenericRelation(Activitys ,related_query_name='Comment-likes')

	updated = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now=True)

	objects = CommentsManerger()
	class Meta:
		verbose_name_plural = "Comments"

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

	def childer(self):
		return Comments.objects.filter(parent=self)
		
	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True