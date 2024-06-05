from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('DOKTOR ÖĞRETİM ÜYESİ ÖN BAŞVURU TARİHLERİ', 'DOKTOR ÖĞRETİM ÜYESİ ÖN BAŞVURU TARİHLERİ'),
        ('DOÇENTLİK ÖN BAŞVURU TARİHLERİ', 'DOÇENTLİK ÖN BAŞVURU TARİHLERİ'),
        ('PROFESÖRLÜK ÖN BAŞVURU TARİHLERİ', 'PROFESÖRLÜK ÖN BAŞVURU TARİHLERİ'),
        ('DOKTOR ÖĞRETİM ÜYESİ BAŞVURU TARİHLERİ', 'DOKTOR ÖĞRETİM ÜYESİ BAŞVURU TARİHLERİ'),
        ('DOÇENTLİK BAŞVURU TARİHLERİ', 'DOÇENTLİK BAŞVURU TARİHLERİ'),
        ('PROFESÖRLÜK BAŞVURU TARİHLERİ', 'PROFESÖRLÜK BAŞVURU TARİHLERİ'),
    ]

    ad = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='DOKTOR ÖĞRETİM ÜYESİ ÖN BAŞVURU')
    bastarih = models.DateField(verbose_name="Başlangıç Tarihi")
    bittar = models.DateField(verbose_name="Bitiş Tarihi")
    düzenleyen = models.TextField(verbose_name="Düzenleyen", default="")
    aciklama = models.TextField(verbose_name="Açıklama")

