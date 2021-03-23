from django.shortcuts import render

# Create your views here.
from .serializers import BeaconSerializer, ModulSerializer, OdaSerializer
from beacon.models import Beacon, AlgilayiciModul, Oda

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView


class BeaconList(ListAPIView):
    serializer_class = BeaconSerializer
    queryset = Beacon.objects.all()


class BeaconDetail(RetrieveAPIView):
    serializer_class = BeaconSerializer
    queryset = Beacon.objects.all()
    lookup_field = 'id'


class BeaconCreate(CreateAPIView):
    serializer_class = BeaconSerializer
    queryset = Beacon.objects.all()


class BeaconUpdate(RetrieveUpdateAPIView):
    serializer_class = BeaconSerializer
    queryset = Beacon.objects.all()
    lookup_field = 'id'


class BeaconDelete(DestroyAPIView):
    serializer_class = BeaconSerializer
    queryset = Beacon.objects.all()
    lookup_field = 'id'


class ModulList(ListAPIView):
    serializer_class = ModulSerializer
    queryset = AlgilayiciModul.objects.all()


class ModulDetail(RetrieveAPIView):
    serializer_class = ModulSerializer
    queryset = AlgilayiciModul.objects.all()
    lookup_field = 'id'


class ModulCreate(CreateAPIView):
    serializer_class = ModulSerializer
    queryset = AlgilayiciModul.objects.all()


class ModulUpdate(RetrieveUpdateAPIView):
    serializer_class = ModulSerializer
    queryset = AlgilayiciModul.objects.all()
    lookup_field = 'id'


class ModulDelete(DestroyAPIView):
    serializer_class = ModulSerializer
    queryset = AlgilayiciModul.objects.all()
    lookup_field = 'id'


class RoomList(ListAPIView):
    serializer_class = OdaSerializer
    queryset = Oda.objects.all()


class RoomDetail(RetrieveAPIView):
    serializer_class = OdaSerializer
    queryset = AlgilayiciModul.objects.all()
    lookup_field = 'id'

class RoomCreate(CreateAPIView):
    serializer_class = OdaSerializer
    queryset = Oda.objects.all()

class RoomUpdate(RetrieveUpdateAPIView):
    serializer_class = OdaSerializer
    queryset = AlgilayiciModul.objects.all()
    lookup_field = 'id'

class RoomDelete(DestroyAPIView):
    serializer_class = OdaSerializer
    queryset = AlgilayiciModul.objects.all()
    lookup_field = 'id'