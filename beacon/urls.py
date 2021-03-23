from django.contrib import admin
from django.urls import path, re_path
from .views import add_beacon, beacon_list, beacon_update, beacon_delete, beacon_detail, add_room, room_delete, \
    room_list, room_detail, room_update, \
    add_modul, \
    modul_update, modul_delete, modul_detail, modul_list

urlpatterns = [
    path('beacon-list', beacon_list, name='beacon-list'),
    path('room-list/', room_list, name='room-list'),
    path('modul-list/', modul_list, name='modul-list'),
    path('add-beacon/', add_beacon, name='add-beacon'),
    path('add-room/', add_room, name='add-room'),
    path('add-modul/', add_modul, name='add-modul'),
    re_path(r'beacon-delete/(?P<pk>[0-9]+)/$', beacon_delete, name='beacon-delete'),
    re_path(r'beacon-update/(?P<pk>[0-9]+)/$', beacon_update, name='beacon-update'),
    re_path(r'beacon-detail/(?P<pk>[0-9]+)/$', beacon_detail, name='beacon-detail'),
    re_path(r'room-delete/(?P<pk>[0-9]+)/$', room_delete, name='room-delete'),
    re_path(r'room-update/(?P<pk>[0-9]+)/$', room_update, name='room-update'),
    re_path(r'room-detail/(?P<pk>[0-9]+)/$', room_detail, name='room-detail'),
    re_path(r'modul-delete/(?P<pk>[0-9]+)/$', modul_delete, name='modul-delete'),
    re_path(r'modul-update/(?P<pk>[0-9]+)/$', modul_update, name='modul-update'),
    re_path(r'modul-detail/(?P<pk>[0-9]+)/$', modul_detail, name='modul-detail'),

]
