from django import forms
from .models import Personeller, Gorevler
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
import re

YEARS = [x for x in range(1940, 2021)]


class PersonnelForm(forms.ModelForm):
    # sex = forms.ChoiceField(required=True, label='Cinsiyet', choices=Personeller.SEX)
    dogum_tarihi = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    iban = forms.CharField(min_length=5, required=False)
    class Meta:
        model = Personeller
        fields = ['isim', 'soyisim', 'unvan', 'departman',
                  'dogum_tarihi', 'cinsiyet', 'kan_grubu',
                  'iban', 'ssk_no',
                  'beacon']


    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=6, required=True, label='Şifre',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(min_length=6, required=True, label='Şifre Tekrar',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(min_length=11, max_length=11, label='Tc Kimlik No:')
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            self.add_error('password', 'Şifreler eşleşmiyor')
            self.add_error('password_confirm', 'Şifreler eşleşmiyor')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email sistemde kayıtlı')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu TC Kimlik No sistemde mevcut')
        return username

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


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50, label='TC Kimlik No',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, max_length=50, label='Şifre',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('TC Kimlik No veya Şifre hatalı')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            users = User.objects.filter(email__iexact=username)
            if len(users) > 0 and len(users) == 1:
                return users.first().username
        return username
