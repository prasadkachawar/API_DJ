from django.contrib import admin

# Register your models here.
from dj_api import models

admin.site.register(models.UserProfile)
