from django.db import models

# Create your models here.



class Info(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    site_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

