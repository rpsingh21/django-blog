from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.

class ActivitysManager(models.Manager):
	def get_likes(self):
		likes = super(ActivitysManager, self).filter(activity_type='L')
		return likes

	def get_favorites(self):
		likes = super(ActivitysManager, self).filter(activity_type='F')
		return likes

	def get_up_votes(self):
		likes = super(ActivitysManager, self).filter(activity_type='U')
		return likes

	def get_down_votes(self):
		likes = super(ActivitysManager, self).filter(activity_type='D')
		return likes



class Activitys(models.Model):
	FAVORITE = 'F'
	LIKE = 'L'
	UP_VOTE = 'U'
	DOWN_VOTE = 'D'
	ACTIVITY_TYPES = (
		(FAVORITE, 'Favorite'),
		(LIKE, 'Like'),
		(UP_VOTE, 'Up Vote'),
		(DOWN_VOTE, 'Down Vote'),
	)

	user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True)
	activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
	date = models.DateTimeField(auto_now_add=True)

	# Below the mandatory fields for generic relation
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type','object_id')

	objects = ActivitysManager()

	class Meta:
		verbose_name_plural = "Activitys"

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username
