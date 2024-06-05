# Generated by Django 4.1.7 on 2023-05-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yardimci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=20, verbose_name='Ad')),
                ('soyad', models.CharField(max_length=20, verbose_name='Soyad')),
                ('email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('telefon', models.CharField(max_length=15, verbose_name='Telefon')),
                ('makale', models.FileField(upload_to='makaleler/', verbose_name='Makale')),
                ('yds_sonuc_belgesi', models.FileField(upload_to='yds_belgeleri/', verbose_name='YDS Sonuç Belgesi')),
            ],
        ),
    ]
