from django.contrib import admin
from profiles_api import models
# Register your models here.
admin.site.register(models.userProfile)
admin.site.register(models.ProfileFeedItem)