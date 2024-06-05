from django.db import models


class Profesor(models.Model):
    ad = models.CharField(max_length=20, verbose_name='Ad')
    soyad = models.CharField(max_length=20, verbose_name='Soyad')
    email = models.EmailField(max_length=30, verbose_name='E-mail')
    telefon= models.CharField(max_length=15, verbose_name='Telefon')
    özgeçmiş = models.FileField(upload_to='profesorCV/',verbose_name="Özgeçmiş",null=True, blank=True)
    yds = models.FileField(upload_to='profesor_yds_belge/',verbose_name="Yabancı Dil Sınav Sonuç Belgesi",null=True,blank=True)
    onay = models.FileField(upload_to='profesoronay/',verbose_name="Onay Belgesi",null=True,blank=True)
    AYOK2 = models.FileField(upload_to='profesorAYOK/',verbose_name="AYÖK belgesi",null=True, blank=True)
    tez = models.FileField(upload_to='profesortezler/',verbose_name="Tez",null=True,blank=True)



