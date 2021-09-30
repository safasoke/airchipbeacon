from django.contrib import admin
from django.urls import path, re_path
from .views import add_personnel, personnel_detail, add_task, personnel_update, personnel_delete, personnel_list, \
    search_auto, user_login, user_logout, user_settings, user_profile, user_about, user_password_change

urlpatterns = [
    path('', personnel_list, name='personnel-list'),
    path('add-personnel/', add_personnel, name='add-personnel'),
    path('search-auto/', search_auto, name='search-auto'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('settings/', user_settings, name='user-settings'),
    path('password-change/', user_password_change, name='user-password-change'),
    re_path(r'personnel-delete/(?P<pk>[0-9]+)/$', personnel_delete, name='personnel-delete'),
    re_path(r'personnel-update/(?P<pk>[0-9]+)/$', personnel_update, name='personnel-update'),
    re_path(r'personnel-detail/(?P<pk>[0-9]+)/$', personnel_detail, name='personnel-detail'),
    re_path(r'add-task/(?P<pk>[0-9]+)/$', add_task, name='add-task'),
    re_path(r'(?P<username>[-\w]+)/about/$', user_about, name='user-aboutme'),
    path(r'(?P<username>[-\w]+)/$', user_profile, name='user-profile')
]
