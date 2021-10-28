from django.urls import path

from RE_user.views import get_agent_list, get_agent_profile

urlpatterns = [
    path('agent-list', get_agent_list, name='agent-list'),
    path('agent-profile/<agent_id>', get_agent_profile, name='agent-profile'),



]