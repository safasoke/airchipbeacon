from django.urls import path,re_path

from django.conf.urls import include, url
from rest_beacon import views

urlpatterns=[
    path('beacon-list/', views.BeaconList.as_view(), name='api-beacon-list'),
    path('beacon-create/', views.BeaconCreate.as_view(), name='api-beacon-create'),
    path('modul-list/', views.ModulList.as_view(), name='api-modul-list'),
    path('modul-create/', views.ModulCreate.as_view(), name='api-modul-create'),
    path('room-list/', views.RoomList.as_view(), name='api-room-list'),
    path('room-create/', views.RoomCreate.as_view(), name='api-room-create'),
    re_path(r'beacon-detail/(?P<id>[0-9]+)/$', views.BeaconDetail.as_view(), name='api-beacon-detail'),
    re_path(r'beacon-update/(?P<id>[0-9]+)/$', views.BeaconUpdate.as_view(), name='api-beacon-update'),
    re_path(r'beacon-delete/(?P<id>[0-9]+)/$', views.BeaconDelete.as_view(), name='api-beacon-delete'),
    re_path(r'modul-detail/(?P<id>[0-9]+)/$', views.ModulDetail.as_view(), name='api-modul-detail'),
    re_path(r'modul-update/(?P<id>[0-9]+)/$', views.ModulUpdate.as_view(), name='api-modul-update'),
    re_path(r'modul-delete/(?P<id>[0-9]+)/$', views.ModulDelete.as_view(), name='api-modul-delete'),
    re_path(r'room-detail/(?P<id>[0-9]+)/$', views.RoomDetail.as_view(), name='api-room-detail'),
    re_path(r'room-update/(?P<id>[0-9]+)/$', views.RoomUpdate.as_view(), name='api-room-update'),
    re_path(r'room-delete/(?P<id>[0-9]+)/$', views.RoomDelete.as_view(), name='api-room-delete'),
]