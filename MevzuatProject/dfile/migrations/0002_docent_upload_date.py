# Generated by Django 4.1.7 on 2023-07-05 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docent',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yükleme Tarihi'),
        ),
    ]
