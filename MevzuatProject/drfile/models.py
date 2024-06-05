from django.db import models
from django.utils import timezone

class Yardimci(models.Model):

    ad = models.CharField(max_length=20, verbose_name='Ad')
    soyad = models.CharField(max_length=20, verbose_name='Soyad')
    email = models.EmailField(max_length=30, verbose_name='E-mail')
    telefon = models.CharField(max_length=15, verbose_name='Telefon')
    onay = models.FileField(upload_to='onay/', verbose_name="Onaylı Doçentlik Belgesi",default="")
    ozgecmis = models.FileField(upload_to='CV/', verbose_name="Özgeçmiş",default="")
    AYOK = models.FileField(upload_to='AYOK/', verbose_name="AYÖK belgesi",default="")
    tez = models.FileField(upload_to='tezler/', verbose_name='Tez',default="")
    yds = models.FileField(upload_to='yd_belge/', verbose_name='Yabancı Dil Sınav Sonuç Belgesi',default="")
    upload_date = models.DateTimeField(verbose_name="Yükleme Tarihi", default=timezone.now)


