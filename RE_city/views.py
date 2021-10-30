from django.shortcuts import render

# Create your views here.
from RE_city.models import City
from RE_property.models import Property


def load_city():
    items = Property.objects.all()
    for item in items:
        obj = City.objects.filter(name__exact=item.city)
        if obj.count() == 0:
            City(name=item.city).save()
    return