from django.contrib import admin
from django.urls import path, re_path
from .views import add_personnel, personnel_detail, add_task, personnel_update, personnel_delete, personnel_list, search_auto, user_login

urlpatterns = [
    path('', personnel_list, name='personnel-list'),
    path('add-personnel/', add_personnel, name='add-personnel'),
    path('search-auto/', search_auto, name='search-auto'),
    path('login/', user_login, name='user-login'),
    re_path(r'personnel-delete/(?P<pk>[0-9]+)/$', personnel_delete, name='personnel-delete'),
    re_path(r'personnel-update/(?P<pk>[0-9]+)/$', personnel_update, name='personnel-update'),
    re_path(r'personnel-detail/(?P<pk>[0-9]+)/$', personnel_detail, name='personnel-detail'),
    re_path(r'add-task/(?P<pk>[0-9]+)/$', add_task, name='add-task')

]
