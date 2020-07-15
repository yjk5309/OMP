from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^place/$', SearchStoreView, name='search_store'),
    re_path(r'^book/$', SearchBookView, name='search_book'),
    re_path(r'^book_result/$', SearchBookResultView, name='search_book_result'),
    re_path(r'^mypage/$', MypageView, name='mypage'),
    re_path(r'^ajax_get_city/$', AjaxGetCityView, name='ajax_get_city'),
]
