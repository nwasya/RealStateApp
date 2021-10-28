from django.urls import path

from RE_account.views import login_page, log_out
from RE_property.views import search_for_property, get_property_detail, save_property, delete_property, AllProperty, \
    MostViewedProperty, RecentProperty

urlpatterns = [
    path('property-items', search_for_property, name='property-items'),
    path('property-details/<property_id>', get_property_detail, name='get_property_detail'),
    path('add-property/<property_id>', save_property, name='add-property'),
    path('delete-property/<property_id>', delete_property, name='delete_property'),
    path('property-items/all', AllProperty.as_view(), name='property-items-all'),
    path('property-items/moset-viewed', MostViewedProperty.as_view(), name='property-items-most-viewed'),
    path('property-items/latest', RecentProperty.as_view(), name='property-items-latest'),




]
