from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here
class Tags(models.Model):
	name=models.CharField(max_length=32)
	description=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Tags"
		ordering=["timestamp"]

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

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

	class Meta:
		verbose_name_plural = "Activitys"

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username


def upload_location(instance,filename):
	return "%s/%s"%(instance.id, filename)

class Posts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	tag=models.ManyToManyField(Tags,blank=True)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	image = models.ImageField(upload_to=upload_location,
							height_field='height_field',
							width_field='width_field',
							blank=True,null=True);
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	activity = GenericRelation(Activitys ,related_query_name='post-likes')
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Posts"
		ordering = ["-updated","-timestamp"]

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Posts.objects.filter(slug=slug).order_by("-id")
	if qs.exists():
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Posts)