# Generated by Django 4.1.7 on 2023-05-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yardimci', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yardimci',
            name='makale',
        ),
        migrations.RemoveField(
            model_name='yardimci',
            name='yds_sonuc_belgesi',
        ),
        migrations.AddField(
            model_name='yardimci',
            name='AYOK',
            field=models.FileField(default='default_ayok.pdf', upload_to='AYOK/', verbose_name='AYÖK belgesi'),
        ),
        migrations.AddField(
            model_name='yardimci',
            name='onay',
            field=models.FileField(default='default_onay.pdf', upload_to='onay/', verbose_name='Onaylı Doçentlik Belgesi'),
        ),
        migrations.AddField(
            model_name='yardimci',
            name='tez',
            field=models.FileField(default='default_tez.pdf', upload_to='tezler/', verbose_name='Tez'),
        ),
        migrations.AddField(
            model_name='yardimci',
            name='yds',
            field=models.FileField(default='default_YDS.pdf', upload_to='yd_belge/', verbose_name='Yabancı Dil Belgesi'),
        ),
        migrations.AddField(
            model_name='yardimci',
            name='özgeçmiş',
            field=models.FileField(default='default_CV.pdf', upload_to='CV/', verbose_name='CV'),
        ),
    ]
