from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
)
from beacon.models import Beacon, Oda, AlgilayiciModul


class BeaconSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name='beacon-api:api-beacon-detail',
    lookup_field='id'
    )
    class Meta:
        model = Beacon
        fields = ['url','id', 'uuid', 'major', 'minor', 'modul']


class ModulSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name='beacon-api:api-modul-detail',
    lookup_field='id'
    )
    class Meta:
        model = AlgilayiciModul
        fields = ['url','id', 'isim', 'oda']


class OdaSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name='beacon-api:api-room-detail',
    lookup_field='id'
    )
    class Meta:
        model = Oda
        fields = ['url','id', 'isim']
