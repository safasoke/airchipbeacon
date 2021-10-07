from django.shortcuts import render

# Create your views here.

from .serializers import PersonnelSerializer, TasksSerializer
from personel.models import Personeller, Gorevler

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView


class PersonnelList(ListAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personeller.objects.all()


class PersonnelDetail(RetrieveAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personeller.objects.all()
    lookup_field = 'id'


class PersonnelCreate(CreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personeller.objects.all()


class PersonnelUpdate(RetrieveUpdateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personeller.objects.all()
    lookup_field = 'id'


class PersonnelDelete(DestroyAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personeller.objects.all()
    lookup_field = 'id'


class TasksList(ListAPIView):
    serializer_class = TasksSerializer
    queryset = Gorevler.objects.all()


class TasksDetail(RetrieveAPIView):
    serializer_class = TasksSerializer
    queryset = Gorevler.objects.all()
    lookup_field = 'id'


class TasksCreate(CreateAPIView):
    serializer_class = TasksSerializer
    queryset = Gorevler.objects.all()


class TasksUpdate(RetrieveUpdateAPIView):
    serializer_class = TasksSerializer
    queryset = Gorevler.objects.all()
    lookup_field = 'id'


class TasksDelete(DestroyAPIView):
    serializer_class = TasksSerializer
    queryset = Gorevler.objects.all()
    lookup_field = 'id'
