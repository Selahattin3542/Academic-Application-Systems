from django.db import models
from django.utils import timezone

class Docent(models.Model):
    ad = models.CharField(max_length=20, verbose_name='Ad')
    soyad = models.CharField(max_length=20, verbose_name='Soyad')
    email = models.EmailField(max_length=30, verbose_name='E-mail')
    telefon= models.CharField(max_length=15, verbose_name='Telefon')
    onay=models.FileField(upload_to='docentonay/',default="")
    ozgecmis = models.FileField(upload_to='docentCV/',default="")
    AYOK = models.FileField(upload_to='docentAYOK/',default="")
    form3=models.FileField(upload_to="docentform3/",verbose_name="FORM-3",default="")
    form4=models.FileField(upload_to="docentform4/",verbose_name="FORM-4",default="")
    tez = models.FileField(upload_to='docenttezler/',default="")
    form7=models.FileField(upload_to='docentform7/',verbose_name="FORM-7",default="")
    yds = models.FileField(upload_to='docentyds_belge/',verbose_name="YDS Sonuç Belgesi",default="")
    upload_date = models.DateTimeField(verbose_name="Yükleme Tarihi", default=timezone.now)

