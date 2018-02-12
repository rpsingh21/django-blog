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


def upload_location(instance, filename):
    return "pofile/%s/%s" % (instance.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=upload_location, height_field='height_field', width_field='width_field', blank=True, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    gender = models.CharField(max_length=8, choices=gender, null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    pin_code = models.CharField(max_length=6, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timeStamps = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


socialSite = (
    ('facebook', 'facebook'),
    ('twitter', 'twitter'),
    ('github', 'github'),
    ('stackoverflow', 'stack overflow'),
    )
