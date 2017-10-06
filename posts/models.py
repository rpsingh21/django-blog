from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from markdownx.utils import markdownify

from activitys.models import Activitys
from comments.models import Comments
from .utils import get_read_time ,conv_thumbnail
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

def upload_location(instance,filename):
	return "%s/%s"%(instance.id, filename)

class Posts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=160)
	tags = models.ManyToManyField(Tags,blank=True)
	slug = models.SlugField(unique=True)
	content = models.TextField()
	image = models.ImageField(upload_to=upload_location,
							height_field='height_field',
							width_field='width_field',
							blank=True,null=True);
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	views=models.BigIntegerField(default=0)
	draft = models.BooleanField(default=False)
	read_time = models.IntegerField(default=0)

	activitys = GenericRelation(Activitys ,related_query_name='activitys')

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

	def comments_count(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return Comments.objects.filter(object_id=self.id,content_type=content_type).count()

	def get_markdown(self):
		content = self.content
		# markdown_text = markdown(content)
		# return mark_safe(markdown_text)
		markdown_text = markdownify(content)
		return mark_safe(markdown_text)
		return content

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type


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
	if instance.content:
		html_string = instance.get_markdown()
		read_time_var = get_read_time(html_string)
		instance.read_time = read_time_var

def post_save_post_receiver(sender,instance,*args,**kwargs):
	conv_thumbnail(instance.image,(768,1024))

pre_save.connect(pre_save_post_receiver, sender=Posts)
post_save.connect(post_save_post_receiver,sender=Posts)