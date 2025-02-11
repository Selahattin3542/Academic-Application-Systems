# Generated by Django 4.1.7 on 2023-06-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0002_remove_profesor_makale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='AYOK',
            field=models.FileField(blank=True, null=True, upload_to='AYOK/', verbose_name='AYÖK belgesi'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='onay',
            field=models.FileField(blank=True, null=True, upload_to='onay/', verbose_name='Onaylı Doçentlik Belgesi'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='tez',
            field=models.FileField(blank=True, null=True, upload_to='tezler/', verbose_name='Tez'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='yds',
            field=models.FileField(blank=True, null=True, upload_to='yd_belge/', verbose_name='Yabancı Dil Belgesi'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='özgeçmiş',
            field=models.FileField(blank=True, null=True, upload_to='CV/', verbose_name='CV'),
        ),
    ]
