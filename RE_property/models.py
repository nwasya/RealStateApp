import os
from datetime import time, datetime

from django.db import models

# Create your models here.
from django.db.models import Q
from django.utils import timezone

from RE_user.models import SiteUser

type = [('restaurant', 'رستوران'),
        ('house', 'خانه'),
        ('garden', 'باغ'),
        ('villa', 'ویلا'),
        ('apartment', 'آپارتمان'),
        ('store', 'مغازه'),
        ]
features = [('cooling', 'کولر'),
            ('heater', 'بخاری'),
            ('refrigerator', 'یخچال'),
            ('washer', 'ظرف شویی'),
            ('lawn', 'حیاط'),
            ('barbeque', 'منقل'),
            ('sauna', 'سونا'),
            ('wifi', 'وای فای'),
            ('cabinet', 'کابینت'),
            ('microwave', 'مایکروویو'),
            ('pool', 'استخر'),
            ('window', 'پرده'),
            ('gym', 'سالن ورزشی'),
            ('phone', 'تلفن'),
            ('antenna', 'آنتن'),
            ('villa', 'ویلا'),
            ]

status = [('rent', 'اجاره'),
          ('sale', 'فروش'),
          ('exchange', 'معاوضه'),
          ]


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


class PropertyManager(models.Manager):
    def search_property(self, filters: dict):
        items = Property.objects.filter(

            Q(city__contains=filters['city']) | Q(part__contains=filters['area']) | Q(
                status__title__contains=filters['status']),
            Q(type__title__contains=filters['type']) |
            (Q(area__lte=filters['size_end']) & Q(area__gte=filters['size_start'])) |
            (Q(price__lte=filters['price_end']) & Q(price__gte=filters['price_start']))

        )
        # Q(bedroom__exact=filters['bedroom']) | Q(
        #                 garage__exact=filters['garage']),

        return items


class Type(models.Model):
    title = models.CharField(max_length=15)
    value = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Features(models.Model):
    title = models.CharField(max_length=15)
    value = models.CharField(max_length=15)

    def __str__(self):
        return self.title



class Status(models.Model):
    title = models.CharField(max_length=15)
    value = models.CharField(max_length=15)

    def __str__(self):
        return self.title



class Property(models.Model):
    title = models.CharField(max_length=20,unique=True)
    property_id = models.IntegerField()
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    type = models.ManyToManyField(Type,null=True)

    status = models.ManyToManyField(Status,null=True)

    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()
    garage_area = models.IntegerField()
    garage_unit = models.CharField(max_length=20)
    area_unit = models.CharField(max_length=20)
    price = models.IntegerField(null=False)
    sec_price = models.IntegerField(null=True)
    monthly_price = models.IntegerField(null=True)
    address = models.CharField(max_length=300)
    garage = models.IntegerField()
    description = models.TextField(max_length=900)
    short_description = models.TextField(max_length=249)

    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    videos = models.TextField(max_length=1000,null=True)
    videos2 = models.TextField(max_length=1000,null=True)
    videos3 = models.TextField(max_length=1000,null=True)
    postal = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    part = models.CharField(max_length=35)
    year = models.CharField(max_length=4)

    features = models.ManyToManyField(Features,null=True)

    is_slider = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    viewed_count = models.IntegerField(null=True)
    added_date = models.DateTimeField(default=timezone.now())
    objects = PropertyManager()

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    Property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_image_path)

    def __str__(self):
        return self.Property.title
