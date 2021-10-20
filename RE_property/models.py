import os
from datetime import time, datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q

property_type = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class PropertyManager(models.Manager):
    def search_property(self, filters: dict):
        items = Property.objects.filter(

            Q(city__contains=filters['city']) | Q(area__contains=filters['area']) | Q(
                status__contains=filters['status']),
            Q(type__contains=filters['type']) |
            (Q(size__lte=filters['size_end']) & Q(size__gte=filters['size_start'])) |
            (Q(price__lte=filters['price_end']) & Q(price__gte=filters['price_start']))

        )
        # Q(bedroom__exact=filters['bedroom']) | Q(
        #                 garage__exact=filters['garage']),

        return items


class Property(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    type = models.CharField(
        max_length=10,

        choices=[('restaurant', 'رستوران'),
                 ('house', 'خانه'),
                 ('garden', 'باغ'),
                 ('villa', 'ویلا'),
                 ('apartment', 'آپارتمان'),
                 ('store', 'مغازه'),
                 ],

    )
    status = models.CharField(
        max_length=10,
        choices=[('rent', 'اجاره'),
                 ('sale', 'فروش'),
                 ('exchange', 'معاوضه'),
                 ],

    )
    bedroom = models.IntegerField(max_length=10)
    floor = models.IntegerField(max_length=10)
    size = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=300)
    garage = models.IntegerField()
    description = models.CharField(max_length=700)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    videos = models.CharField(max_length=20)
    is_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    viewed_count = models.IntegerField()
    added_date = models.DateTimeField(default=datetime.now())
    objects = PropertyManager()




class PropertyImage(models.Model):
    Property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_image_path)

    def __str__(self):
        return self.Property.title


class PropertyVideo(models.Model):
    Property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    video_link = models.CharField(max_length=600)

    def __str__(self):
        return self.Property.title
