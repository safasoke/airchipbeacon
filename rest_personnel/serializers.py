from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
)
from personel.models import Personeller, Gorevler


class PersonnelSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='personnel-api:api-personnel-detail',
        lookup_field='id'
    )

    class Meta:
        model = Personeller
        fields = ['url', 'id', 'isim', 'soyisim', 'tc_kimlik_no', 'cinsiyet', 'dogum_tarihi', 'beacon']


class TasksSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='personnel-api:api-personnel-detail',
        lookup_field='id'
    )

    class Meta:
        model = Personeller
        fields = ['url', 'id', 'isim', 'soyisim', 'tc_kimlik_no', 'cinsiyet', 'dogum_tarihi', 'beacon']
