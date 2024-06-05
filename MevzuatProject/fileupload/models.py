from django.db import models
from django.utils import timezone

class Document(models.Model):
    CATEGORY_CHOICES =[

        ('A-1a', 'A-1a'),
        ('A-1b', 'A-1b'),
        ('A-2a', 'A-2a'),
        ('C-1', 'C-1'),
        ('B-1', 'B-1'),
        ('B-2', 'B-2'),
        ('D-1', 'D-1'),
        ('D-2', 'D-2'),
        ('E-1', 'E-1'),
        ('K', 'K'),
        ('L', 'L'),
        ('M', 'M'),
    ]

    CATEGORY_CHOICES1=[
        ('Makale','Makale'),
        ('Tez','Tez'),
        ('Kitap', 'Kitap'),
        ('Bildiri','Bildiri'),
        ('Patent','Patent'),
         ('Rapor','Rapor'),
        ('Editörlük','Editörlük'),
        ('Teknik notlar','Teknik notlar'),
        ('Araştırma mektupları','Araştırma mektupları'),
        ('Derleme makaleleri', 'Derleme makaleleri')

    ]

    CATEGORY_CHOICES2 = [
        ('Doktor Öğretim Üyesi Ön Başvuru','Doktor Öğretim Üyesi Ön Başvuru'),
        ('Doçent Ön Başvuru', 'Doçent Ön Başvuru'),
        ('Profesör Ön Başvuru', 'Profesör Ön Başvuru'),
        ('Doktor Öğretim Üyesi Başvuru', 'Doktor Öğretim Üyesi  Başvuru'),
        ('Doçent Başvuru','Doçent Başvuru'),
        ('Profesör Başvuru', 'Profesör Başvuru'),



    ]

    ad= models.CharField(max_length=100,verbose_name="Ad",default="")
    soyad = models.CharField(max_length=100,verbose_name="Soyad",default="")
    basvurulanbolum=models.CharField(max_length=100, choices=CATEGORY_CHOICES2,default="Doktor Öğretim Üyesi Ön Başvuru",verbose_name="Başvurulan Program")
    yayinadi=models.CharField(max_length=100, choices=CATEGORY_CHOICES1,default="Makale",verbose_name="Yayın Adı")
    yayinturu = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default="A1-a",verbose_name="Yayın Türü")
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(verbose_name="Yükleme Tarihi", default=timezone.now)
