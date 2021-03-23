from django import forms
from .models import Personeller, Gorevler

YEARS = [x for x in range(1940, 2021)]


class PersonnelForm(forms.ModelForm):
    # sex = forms.ChoiceField(required=True, label='Cinsiyet', choices=Personeller.SEX)
    dogum_tarihi = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    tc_kimlik_no = forms.CharField(min_length=11, max_length=11)
    iban = forms.CharField(min_length=24, required=False)

    class Meta:
        model = Personeller
        fields = ['isim', 'soyisim', 'unvan', 'departman', 'tc_kimlik_no', 'dogum_tarihi', 'cinsiyet', 'kan_grubu',
                  'iban', 'ssk_no',
                  'beacon']

    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Gorevler
        fields = ['gorev_adi', 'gorev']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
            self.fields['gorev'].widget.attrs['rows'] = 4


class PersonnelSearch(forms.Form):
    search = forms.CharField(required=False, max_length=500, widget=forms.TextInput(
        attrs={'placeholder': 'Personel arayın', 'class': 'form-control', 'id': 'personnel'}))
