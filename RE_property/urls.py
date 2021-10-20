from django.urls import path

from RE_account.views import login_page, log_out
from RE_property.views import search_for_property

urlpatterns = [
    path('property-items', search_for_property, name='property-items'),




]
