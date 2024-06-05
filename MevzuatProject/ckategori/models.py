
from django.db import models


class Category(models.Model):
    # Define a dictionary of category choices for each group
    CATEGORY_CHOICES = {
        'E1': [
            ('10/15', '10/15'), ('4','4')
        ],
        'E2': [
            ('5','5'), ('3', '3')
        ],
        'F1': [
            ('50','50')
        ],
        'F2': [
            ('20', '20'), ('5', '5'),
        ],
        'F3': [
            ('20', '20')
        ],
        'F4': [
            ('25','25'),('15','15'),('5','5')
        ],
        'G1:(ATIFLAR)': [
            ('3','3'),
        ],
        'G2': [
            ('1', '1')
        ],
        'G3': [
            ('1', '1'),
        ],
        'G4': [
            ('4', '4'),
        ],
        'H1': [
            ('4', '4'),
        ],
        'H2': [
            ('1/2', '1/2'),
        ],
        'H3': [
            ('3', '3'),
        ],
        'H4': [
            ('10/5', '10/5'),
        ]



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