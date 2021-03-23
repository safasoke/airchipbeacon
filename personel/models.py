from django.db import models
from beacon.models import Beacon
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.

class Personeller(models.Model):
    SEX = ((None, 'Cinsiyet Seçiniz'), ('bos', 'Belirtmek İstemiyorum'), ('erkek', 'Erkek'), ('kadin', 'Kadın'))
    KANGRUBU = (
        (None, 'Kan Grubu Seçini'), ('bos', 'Belirtmek İstemiyorum'), ('0RhPozitif', '0 Rh+'), ('0RhNegatif', '0 Rh-'),
        ('abRhPozitif', 'AB Rh+'), ('abRhNegatif', 'AB Rh-'), ('aRhPozitif', 'A Rh+'), ('aRhNegatif', 'A Rh-'),
        ('bRhPozitif', 'B Rh+'), ('bRhNegatif', 'B Rh-'))
    user = models.OneToOneField(User, null=True, blank=False, verbose_name='User', on_delete=models.CASCADE)
    isim = models.CharField(max_length=50, verbose_name='İsim', blank=False, null=True)
    soyisim = models.CharField(max_length=50, verbose_name='Soyisim', blank=False, null=True)
    unvan = models.CharField(max_length=50, verbose_name='Ünvan', blank=True, null=True)
    departman = models.CharField(max_length=50, verbose_name='Departman', blank=True, null=True)
    tc_kimlik_no = models.CharField(max_length=11, verbose_name='TC Kimlik No', blank=False, null=True, unique=True)
    cinsiyet = models.CharField(choices=SEX, blank=False, null=True, max_length=20, verbose_name='Cinsiyet')
    dogum_tarihi = models.DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    kan_grubu = models.CharField(choices=KANGRUBU, verbose_name='Kan Grubu', max_length=30, blank=False, null=True)
    ssk_no = models.CharField(max_length=50, verbose_name='SSK No', blank=True, null=True)
    iban = models.CharField(max_length=24, verbose_name='IBAN Bilgisi', blank=True, null=True)
    beacon = models.OneToOneField(Beacon, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Personeller'
        ordering = ['isim']

    def __str__(self):
        return "%s %s" % (self.isim, self.soyisim)

    def get_personnel_task(self):
        return self.gorevler_set.all()

    def get_absolute_url(self):
        return reverse('personnel-detail', kwargs={'pk': self.pk})


class Gorevler(models.Model):
    gorev_adi = models.CharField(max_length=50, verbose_name='Görev İsmi', blank=True, null=True)
    gorev = models.TextField(max_length=1000, blank=False, verbose_name='Görev Giriniz', null=True)
    personel = models.ForeignKey(Personeller, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Görevler'

    def __str__(self):
        return self.gorev_adi
