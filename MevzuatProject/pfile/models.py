from django.db import models
from django.utils import timezone

class Prof(models.Model):
    ad = models.CharField(max_length=20, verbose_name='Ad')
    soyad = models.CharField(max_length=20, verbose_name='Soyad')
    email = models.EmailField(max_length=30, verbose_name='E-mail')
    telefon= models.CharField(max_length=15, verbose_name='Telefon')
    onay=models.FileField(upload_to='docentonay/',default="")
    ozgecmis = models.FileField(upload_to='docentCV/',verbose_name="Özgeçmiş",default="")
    AYOK2 = models.FileField(upload_to='docentAYOK2/',default="")
    form5=models.FileField(upload_to="profform5/",verbose_name="FORM-5",default="")
    form6=models.FileField(upload_to="profform6/",verbose_name="FORM-6",default="")
    tez = models.FileField(upload_to='docenttezler/',default="")
    form7=models.FileField(upload_to='docentform7/',verbose_name="FORM-7",default="")
    yds = models.FileField(upload_to='docentyds_belge/',verbose_name="YDS Sonuç Belgesi",default="")
    upload_date = models.DateTimeField(verbose_name="Yükleme Tarihi", default=timezone.now)

