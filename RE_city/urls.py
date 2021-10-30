from django.urls import path

from RE_city.views import load_city

urlpatterns = [
    path('load-city', load_city, name='load_city')
]

