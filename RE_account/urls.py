from django.urls import path

from RE_account.views import login_page, log_out

urlpatterns = [
    path('login', login_page, name='login'),
    path('logout', log_out, name='logout'),


]
