from django.urls import path

from RE_account.views import login_page, log_out
from RE_property.views import search_for_property, get_property_detail, save_property

urlpatterns = [
    path('property-items', search_for_property, name='property-items'),
    path('property-details/<property_id>', get_property_detail, name='get_property_detail'),
    path('add-property', save_property, name='add-property'),




]
