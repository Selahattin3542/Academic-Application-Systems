# Generated by Django 4.1.7 on 2023-05-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onprof', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='eser',
        ),
        migrations.RemoveField(
            model_name='application',
            name='eser_türü',
        ),
        migrations.AddField(
            model_name='application',
            name='eser1',
            field=models.FileField(default='defaulr_eser1.pdf', upload_to='eserler/', verbose_name='Başlıca Eser 1'),
        ),
        migrations.AddField(
            model_name='application',
            name='eser2',
            field=models.FileField(default='default_eser2.pdf', upload_to='eserler2/', verbose_name='Başlıca Eser 2'),
        ),
        migrations.AddField(
            model_name='application',
            name='eser3',
            field=models.FileField(default='default_eser3.pdf', upload_to='eserler3/', verbose_name='Başlıca Eser 3'),
        ),
        migrations.AddField(
            model_name='application',
            name='eser_türü1',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1')], default='A1-a', max_length=10, verbose_name='Eser Türü 1'),
        ),
        migrations.AddField(
            model_name='application',
            name='eser_türü2',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1')], default='A2-a', max_length=10, verbose_name='Eser Türü 2'),
        ),
        migrations.AddField(
            model_name='application',
            name='eser_türü3',
            field=models.CharField(choices=[('A-1a', 'A-1a'), ('A-1b', 'A-1b'), ('A-2a', 'A-2a'), ('C-1', 'C-1')], default='A3-a', max_length=10, verbose_name='Eser Türü 3'),
        ),
        migrations.AddField(
            model_name='application',
            name='sözlü',
            field=models.FileField(default='default_sozlu.pdf', upload_to='sözlüler/', verbose_name='Sözlü Sınav'),
        ),
        migrations.AlterField(
            model_name='application',
            name='doktora_tezi',
            field=models.FileField(default='default_tez.pdf', upload_to='tezler/', verbose_name='Doktora Tezi'),
        ),
        migrations.AlterField(
            model_name='application',
            name='makale',
            field=models.FileField(default='default_makale.pdf', upload_to='makaleler/', verbose_name='Makale'),
        ),
        migrations.AlterField(
            model_name='application',
            name='makale_türü',
            field=models.CharField(choices=[('B-1', 'B-1'), ('B-2', 'B-2'), ('D-1', 'D-1'), ('D-2', 'D-2'), ('E-1', 'E-1'), ('K', 'K'), ('L', 'L'), ('M', 'M')], default='B-1', max_length=10, verbose_name='Makale Türü'),
        ),
        migrations.AlterField(
            model_name='application',
            name='tez_türü',
            field=models.CharField(choices=[('B-1', 'B-1'), ('B-2', 'B-2'), ('D-1', 'D-1'), ('D-2', 'D-2'), ('E-1', 'E-1'), ('K', 'K'), ('L', 'L'), ('M', 'M')], default='B-1', max_length=10, verbose_name='Tez Türü'),
        ),
        migrations.AlterField(
            model_name='application',
            name='yds_belge',
            field=models.FileField(default='default_YDS.pdf', upload_to='yds_belgeler/', verbose_name='YDS sınav sonuç belgesi'),
        ),
    ]
