from django.contrib import admin

# Register your models here.
from RE_user.models import SiteUser

admin.site.register(SiteUser)
