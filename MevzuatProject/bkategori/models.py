
from django.db import models


class Category(models.Model):
    # Define a dictionary of category choices for each group
    CATEGORY_CHOICES = {
        'B1': [
            ('13/15', '13/15'), ('5','5')
        ],
        'B2': [
            ('6','6'), ('3', '3')
        ],
        'C1': [
            ('100','100')
        ],
        'C2': [
            ('30', '30'), ('5', '5'),
        ],
        'C3': [
            ('50', '50')
        ],
        'C4': [
            ('40','40'),('30','30'),('10','10')
        ],
        'D1': [
            ('18','18'),('8','8')
        ],
        'D2': [
            ('10', '10'), ('5', '5'),
        ],
        'D3': [
            ('4', '4'),
        ],
        'D4': [
            ('8', '8'),
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
