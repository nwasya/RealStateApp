from django.db import models

# Create your models here.
from RE_news.models import News


class PropertyCommentManager(models.Manager):
    def get_active_comments(self):
        return self.get_queryset().filter(confirmed=True)
    def get_by_id(self, property_id):
        qs = self.get_queryset().filter(id=property_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def set_status_comment(self, propert_id):
        qs = self.get(id=propert_id)
        if qs.confirmed:
            qs.confirmed = False
            qs.save()

        else:
            qs.confirmed = True
            qs.save()





class NewsCommentManager(models.Manager):
    def get_active_comments(self):
        return self.get_queryset().filter(confirmed=True)
    def get_by_id(self, property_id):
        qs = self.get_queryset().filter(id=property_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def set_status_comment(self, propert_id):
        qs = self.get(id=propert_id)
        if qs.confirmed:
            qs.confirmed = False
            qs.save()

        else:
            qs.confirmed = True
            qs.save()


class NewsComment(models.Model):
    full_name = models.CharField(max_length=100,null=False)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(null=False)
    email = models.EmailField(null=False)
    object = models.ForeignKey(News,on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    objects = NewsCommentManager





class PropertyComment(models.Model):
    full_name = models.CharField(max_length=100,null=False)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(null=False)
    email = models.EmailField(null=False)
    object = models.ForeignKey(News,on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    objects = PropertyCommentManager