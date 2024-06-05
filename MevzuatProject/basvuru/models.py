from django.db import models

class Application(models.Model):
    CATEGORY_CHOICES1 = [
        ('A-1a', 'A-1a'),
        ('A-1b', 'A-1b'),
        ('A-2a', 'A-2a'),
        ('A-2b', 'A-2b'),
        ('A-3a', 'A-3a'),
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
    email= models.EmailField(max_length=20,verbose_name="E-mail")
    telefon =models.CharField(max_length=50,verbose_name="Telefon")
    eser = models.FileField(upload_to='eserler/', verbose_name="Başlıca Eser")
    eser_türü = models.CharField(max_length=10, choices=CATEGORY_CHOICES1,verbose_name="Eser Türü")
    makale = models.FileField(upload_to='makaleler/', verbose_name="Makale")
    makale_türü = models.CharField(max_length=10, choices=CATEGORY_CHOICES2,verbose_name="Makale Türü")
    doktora_tezi = models.FileField(upload_to='tezler/', verbose_name="Doktora Tezi")
    tez_türü = models.CharField(max_length=10, choices=CATEGORY_CHOICES2,verbose_name="Tez Türü")
    yds_belge = models.FileField(upload_to='yds_belgeler/',verbose_name="YDS sınav sonuç belgesi")