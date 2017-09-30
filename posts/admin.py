from django.contrib import admin

from .models import Posts ,Tags, Activitys

# Register your models here.
admin.site.register(Posts)
admin.site.register(Tags)
admin.site.register(Activitys)
