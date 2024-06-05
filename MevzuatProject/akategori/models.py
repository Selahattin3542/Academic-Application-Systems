from django.db import models
class Category(models.Model):
    # Define a dictionary of category choices for each group
    CATEGORY_CHOICES = {
        'A-1a(Q1 kategorisindeki dergilerde yayımlanmış özgün araştırma makalesi)': [
             ('50', '50')],
        'A-1b (Q2 kategorisindeki dergilerde yayımlanmış özgün araştırma makalesi ': [
            ('40', '40')],
        'A-1c (Q1/Q2 kategorisindeki dergilerde yayımlanmış Derleme )': [
             ('50', '50'), ('40', '40')],
        'A-1d Q1/Q2 kategorisindeki dergilerde yayımlanmış ‘Short Communication= Brief Communication': [
             ('30', '30')],
        'A-1e Q1/Q2 kategorisindeki dergilerde yayımlanmış kongreye ait (tam metin / bildiri özeti) makale': [
            ('25', '25'), ('12.5', '12.5'), ('20', '20'), ('10', '10')],
        'A-1f Q1/Q2 kategorisindeki dergilerde yayımlanmış Vaka-Vaka Serisi Raporu, Teknik Not,Editöre Mektup, Kitap veya Makale Tahlili, Tartışma': [
             ('25', '25'), ('20', '20')],
        'A-1g Mimarlık, Planlama ve Tasarım Temel Alanı / Sosyal, Beşeri ve İdari Bilimler Temel Alanı için; Alan indeksleri kapsamındaki dergilerde yayımlanmış makale': [
            ('50', '50')],
        'A2-a Q3 kategorisindeki dergilerde yayımlanmış özgün araştırma makalesi': [
             ('30', '30')],
        'A-2b Q4 kategorisindeki dergilerde yayımlanmış özgün araştırma makalesi ': [
             ('20', '20')],
        'A-2c Q3/Q4 kategorisindeki dergilerde yayımlanmış derleme': [
             ('30', '30'), ('20', '20')],
        'A-2d Q3 / Q4 kategorisindeki dergilerde yayımlanmış ‘Short Communication = Brief Communication': [
             ('20', '20'), ('15', '15')],
        'A-2e Q3/Q4 kategorisindeki dergilerde yayımlanmış kongrede basılmış (tam metin / bildiri özeti) makale': [
             ('15-7.5', '15-7.5'), ('10-5', '10-5')],
        'A - 2f Q3 / Q4 kategorisindeki dergilerde yayımlanmış Vaka - Vaka Serisi Raporu, Teknik Not, Editöre Mektup, Kitap veya Makale Tahlili, Tartışma': [
            ('15', '15'), ('10', '10')],
        'A-3a ESCI kategorisindeki dergilerde yayımlanmış özgün araştırma makalesi': [
          ('20', '20')],
        'A-3b ESCI kategorisindeki dergilerde yayımlanmış Derleme, Short Communication=Brief Communication, Vaka/Vaka Serisi Raporu, Teknik Not, Editöre Mektup, Kitap veya Makale Tahlili, Tartışma, Kongreye ait tam metin bildiri': [
             ('10', '10')],
        'A-4a Diğer ulaslararası alan indeksleri kategorisindeki dergilerde yayımlanmış özgün araştırma makalesi': [
             ('15', '15')],
        'A-4b Diğer uluslararası alan indeksleri kategorisindeki dergilerde yayımlanmış Derleme,  Short Communication = Brief Communication, Vaka / Vaka Serisi  Raporu, Teknik Not, Editöre Mektup, Kitap veya Makale Tahlili, Tartışma, Kongreye ait tam metin bildiri': [
        ('7.5', '7.5')],
        'A-5 Diğer uluslararası alan indeksleri kategorisine girmeyen uluslararası dergiler ile Mesleki Kurumsal dergilerde yayımlanan makaleler': [
             ('4', '4')],
        'A-6 Başvurulan bilim alanında Uluslararası özgün tasarım çalışmaları ve sanat eserleri ilejürili olarak fuar, festival, çalıştay (workshop), gösteri, bienal, trienal gibi etkinliğe bir çalışma ile katılmak': [
             ('15', '15')],
    }

    # Create fields dynamically using a loop
    for group, choices in CATEGORY_CHOICES.items():
        for i, choice in enumerate(choices, start=1):
            field_name = f'kategori_{group}_{i}'
            field_verbose_name = f'{group}-{i}'
            locals()[field_name] = models.CharField(
                max_length=20,
                verbose_name=field_verbose_name,
                choices=[choice],
                null=True,
                blank=True
            )