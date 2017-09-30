from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.
gender = (
	('M', 'male'),
	('F', 'female'),
	('T', 'transgendered')
)
class Profile(models.Model):
	user =models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	gender = models.CharField(max_length=8,choices = gender,null=True,blank=True)
	location = models.CharField(max_length=30, blank=True)
	pin_code = models.CharField(max_length=6, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timeStamps = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.user)

	def __str__(self):
		return  str(self.user)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
