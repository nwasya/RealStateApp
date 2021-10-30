from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from RE_property.models import upload_image_path


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    description1 = models.TextField()
    description2 = models.TextField()

    added_date = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    hashtags = models.CharField(max_length=200)
    quote = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def get_description_first_part(self):
        return self.description[:60]

    def get_hashtags_list(self):
        return self.hashtags.split(' ')

    def find_next_new_id(self):
        return self.get_next_by_added_date().id

    def find_previous_new_id(self):
        return self.get_previous_by_added_date().id
