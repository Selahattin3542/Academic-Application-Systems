from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    CATEGORY_CHOICES1 = [
        ('A-1a', 'A-1a'),
        ('A-1b', 'A-1b'),
        ('A-2a', 'A-2a'),
        ('C-1', 'C-1')
        ]
    CATEGORY_CHOICES2=[
        ('B-1', 'B-1'),
        ('B-2', 'B-2'),
        ('D-1', 'D-1'),
        ('D-2', 'D-2'),
        ('E-1', 'E-1'),
        ('K', 'K'),
        ('L', 'L'),
        ('M', 'M'),
    ]
    ad = models.CharField(max_length=50,verbose_name="Ad")
    soyad = models.CharField(max_length=50,verbose_name="Soyad")
    email= models.EmailField(max_length=50,verbose_name="E-mail")
    telefon =models.CharField(max_length=50,verbose_name="Telefon")
    eser1= models.FileField(upload_to='eserler1/',verbose_name="1.eser",default="")
    eser_türü1= models.CharField(max_length=10, choices=CATEGORY_CHOICES1,verbose_name="Eser Türü 1",default="A1-a")
    eser2= models.FileField(upload_to='eserler2/',verbose_name="2.eser",default="")
    eser_türü2 = models.CharField(max_length=10, choices=CATEGORY_CHOICES1, verbose_name="Eser Türü 2",default="A1-a")
    makale = models.FileField(upload_to='makaleler1/',verbose_name="Makale",default="")
    makale_türü = models.CharField(max_length=10, choices=CATEGORY_CHOICES2,verbose_name="Makale Türü",default="B-1")
    doktora_tezi = models.FileField(upload_to='tezler1/',verbose_name="tez",default="")
    tez_türü = models.CharField(max_length=10, choices=CATEGORY_CHOICES2,verbose_name="Tez Türü",default="B-1")
    yds_belge = models.FileField(upload_to='yds_belgeler1/',verbose_name="YDS Sonuç Belgesi",default="")
    sözlü= models.FileField(upload_to='sözlüler1/',verbose_name="Sözlü Sınav Sonuç Belgesi",default="")
    upload_date = models.DateTimeField(verbose_name="Yükleme Tarihi", default=timezone.now)

