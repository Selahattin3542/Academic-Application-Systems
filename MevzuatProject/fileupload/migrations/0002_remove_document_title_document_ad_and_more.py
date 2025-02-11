# Generated by Django 4.1.7 on 2023-07-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.AddField(
            model_name='document',
            name='ad',
            field=models.CharField(default='', max_length=100, verbose_name='Ad'),
        ),
        migrations.AddField(
            model_name='document',
            name='basvurulanbolum',
            field=models.CharField(choices=[('Doktor Öğretim Üyesi Ön Başvuru', 'Doktor Öğretim Üyesi Ön Başvuru'), ('Doçent Ön Başvuru', 'Doçent Ön Başvuru'), ('Profesör Ön Başvuru', 'Profesör Ön Başvuru'), ('Doktor Öğretim Üyesi Başvuru', 'Doktor Öğretim Üyesi  Başvuru'), ('Doçent Başvuru', 'Doçent Başvuru'), ('Profesör Başvuru', 'Profesör Başvuru')], default='Doktor Öğretim Üyesi Ön Başvuru', max_length=100, verbose_name='Başvurulan Program'),
        ),
        migrations.AddField(
            model_name='document',
            name='soyad',
            field=models.CharField(default='', max_length=100, verbose_name='Soyad'),
        ),
        migrations.AddField(
            model_name='document',
            name='yayinadi',
            field=models.CharField(choices=[('Makale', 'Makale'), ('Tez', 'Tez')], default='Makale', max_length=100, verbose_name='Yayın Adı'),
        ),
        migrations.AddField(
            model_name='document',
            name='yayinturu',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1'), ('B-1', 'B-1'), ('B-2', 'B-2'), ('D-1', 'D-1'), ('D-2', 'D-2'), ('E-1', 'E-1'), ('K', 'K'), ('L', 'L'), ('M', 'M')], default='A1-a', max_length=100, verbose_name='Yayın Türü'),
        ),
    ]
