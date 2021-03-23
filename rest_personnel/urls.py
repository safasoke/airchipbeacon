from django.urls import path,re_path

from django.conf.urls import include, url
from rest_personnel import views

urlpatterns = [
    path('personnel-list/', views.PersonnelList.as_view(), name='api-personnel-list'),
    path('personnel-create/', views.PersonnelCreate.as_view(), name='api-personnel-create'),
    path('tasks-list/', views.TasksList.as_view(), name='api-tasks-list'),
    path('tasks-create/', views.TasksCreate.as_view(), name='api-tasks-create'),
    re_path(r'personnel-detail/(?P<id>[0-9]+)/$', views.PersonnelDetail.as_view(), name='api-personnel-detail'),
    re_path(r'personnel-update/(?P<id>[0-9]+)/$', views.PersonnelUpdate.as_view(), name='api-personnel-update'),
    re_path(r'personnel-delete/(?P<id>[0-9]+)/$', views.PersonnelDelete.as_view(), name='api-personnel-delete'),
    re_path(r'tasks-detail/(?P<id>[0-9]+)/$', views.TasksDetail.as_view(), name='api-tasks-detail'),
    re_path(r'tasks-update/(?P<id>[0-9]+)/$', views.TasksUpdate.as_view(), name='api-tasks-update'),
    re_path(r'tasks-delete/(?P<id>[0-9]+)/$', views.TasksDelete.as_view(), name='api-tasks-delete'),
    ]