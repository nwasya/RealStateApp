import os
from datetime import time, datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q
from django.utils import timezone


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class SiteUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=40)
    occupation = models.CharField(max_length=30)
    wtsp = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    telegram = models.CharField(max_length=60,default='null')
    city = models.CharField(max_length=40)
    bio = models.TextField()
    birth = models.IntegerField()
    created_date = models.DateField(default=timezone.now())
    rate = models.IntegerField()
