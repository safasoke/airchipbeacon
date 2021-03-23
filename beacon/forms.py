from django import forms
from .models import Beacon, AlgilayiciModul, Oda


class BeaconForm(forms.ModelForm):
    class Meta:
        model = Beacon
        fields = ['uuid', 'major', 'minor', 'modul']

    def __init__(self, *args, **kwargs):
        super(BeaconForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class RoomForm(forms.ModelForm):
    class Meta:
        model = Oda
        fields = ['isim']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class ModulForm(forms.ModelForm):
    class Meta:
        model = AlgilayiciModul
        fields = ['isim', 'oda']

    def __init__(self, *args, **kwargs):
        super(ModulForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
