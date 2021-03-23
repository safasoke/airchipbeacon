from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Oda(models.Model):
    isim = models.CharField(max_length=50, verbose_name='Oda İsmi', blank=False, null=True)

    class Meta:
        verbose_name_plural = 'Oda'

    def __str__(self):
        return (self.isim)

    def get_absolute_url_room(self):
        return reverse('room-detail', kwargs={'pk': self.pk})

    def get_room_moduls(self):
        return self.algilayicimodul_set.all()


class AlgilayiciModul(models.Model):
    isim = models.CharField(max_length=50, verbose_name='Algılayıcı İsmi', blank=False, null=True)
    oda = models.ForeignKey(Oda, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Algılayıcı Modül'

    def __str__(self):
        return (self.isim)

    def get_absolute_url_modul(self):
        return reverse('modul-detail', kwargs={'pk': self.pk})


class Beacon(models.Model):
    uuid = models.CharField(max_length=128)
    major = models.CharField(max_length=10, blank=True, null=True)
    minor = models.CharField(max_length=10, blank=True, null=True)
    modul = models.ForeignKey(AlgilayiciModul, null=True, blank=True, on_delete=models.CASCADE)
    son_gorulme = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Beacon'

    def __str__(self):
        return (self.uuid)

    def get_absolute_url_beacon(self):
        return reverse('beacon-detail', kwargs={'pk': self.pk})
