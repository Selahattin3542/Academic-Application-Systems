
from django.db import models


class Category(models.Model):
    # Define a dictionary of category choices for each group
    CATEGORY_CHOICES = {
        'M1': [
            ('60/30', '60/30'),
        ],
        'M2': [
            ('50/25', '50/25')
        ],
        'M3': [
            ('40/20', '40/20')
        ],
        'M4': [
            ('15/8', '15/8'),
        ],
        'M5': [
            ('30/15', '30/15')
        ],
        'M6': [
            ('15/5', '15/5')
        ],
        'M7': [
            ('30/15', '30/15'),
        ],
        'M8': [
            ('20/10', '20/10')
        ],
        'N1-Kamu ve/veya özel sektörde, Teknoparklarda ve/veya sanayi kuruluşlarının Ar-ge birimlerinde en az 3 ay süreli danışmanlık hizmeti ve eğiticilik (x ay)': [
            ('2', '2'),
        ],
        'N2-Teknopark ve benzeri alanlarda şirket kurucusu/ortağı olmak ve şirket faaliyetlerine devam ediyor olmak ': [
            ('20', '20'),
        ],
        'N3-Üniversite – Sanayi / Kamu Kurumları işbirliği kapsamında tamamlanmış proje tasarım faaliyetleri': [
            ('5', '5'),
        ],
        'N4-Bilirkişilik faaliyeti (x adet) ': [
            ('2', '2'),
        ],
        'O1-Q kategorisindeki dergilerde yapılan hakemlik (her hakemlik başına)': [
            ('5', '5'),('2','2'),('5','5'),('15','15'),('1','1')
        ],
        'O2-Q kategorisindeki ve dışındaki dergilerde yayın kurulu üyelikleri (x yıl)':[
            ('3','3'),('1','1')
        ],
        'O3-Bilim - Sanat kurulu başkanlığı / üyeliği (x yıl)':[
            ('5/4','5/4')

        ],
        'O4-Uluslararası bir standartın hazırlanmasında görev almak': [
            ('20','20')
        ],
        'O5-Bilimsel / Sanatsal toplantı düzenleme kurul başkanlığı / editörlüğü / kurul üyeliğ':[
            ('20/15/10','20/15/10')
        ],
        'O6-Q1 ve Q2 kategorisindeki dergilerde editör / editör yardımcılığı / editör kurulu üyeliği (x yıl) ': [
            ('20/15/12', '20/15/12'),('15/10/8','15/10/8'),('6/4/3','6/4/3')
        ],
        'O7-(ULUSAL)':[
            ('2','2'),('2','2'),('5/3/2','5/3/2'),('1','1')
        ],
        'O8-Yayın kurulu üyelikleri (x yıl) ': [
            ('1', '1')
        ],
        'O9-Bilim / Sanat kurulu başkanlığı / üyeliği (x yıl) ': [
            ('2/1', '2/1')
        ],
        'O10-Ulusal bir standartın hazırlanmasında görev almak': [
            ('15', '15')
        ],
        'O11-Bilimsel-Sanatsal toplantı düzenleme kurul başkanlığı / editörlüğü / kurul üyeliği':[
            ('10/8/5','10/8/5')
    ],
        'O12-Dergilerde editörlük / editör yardımcılığı / editör kurul üyeliği (x yıl)': [
            ('5/4/3', '5/4/3')
        ],


    }

    # Use a loop to create the fields for each category
    for group in CATEGORY_CHOICES:
        for i, choice in enumerate(CATEGORY_CHOICES[group], start=1):
            # Use the group and index as the field name
            field_name = f'kategori_{group}_{i}'
            # Create the field with the choice and verbose name
            locals()[field_name] = models.CharField(
                max_length=20,
                verbose_name=f'{group}-{i}',
                choices=[choice],
                null=True,
                blank=True

            )


