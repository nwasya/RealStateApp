from django.contrib import admin

# Register your models here.
from RE_comment.models import PropertyComment,NewsComment

admin.site.register(PropertyComment)
admin.site.register(NewsComment)