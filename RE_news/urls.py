from django.urls import path

from RE_account.views import login_page, log_out
from RE_news.views import get_news, get_news_detail

urlpatterns = [
    path('all-news/<id>', get_news, name='get_all_news'),
    path('blog-detail/<id>', get_news_detail, name='get_news_detail'),




]
