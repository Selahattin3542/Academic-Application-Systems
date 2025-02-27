# Generated by Django 4.1.7 on 2023-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_E1_1', models.CharField(blank=True, choices=[('10/15', '10/15')], max_length=20, null=True, verbose_name='E1-1')),
                ('kategori_E1_2', models.CharField(blank=True, choices=[('4', '4')], max_length=20, null=True, verbose_name='E1-2')),
                ('kategori_E2_1', models.CharField(blank=True, choices=[('5', '5')], max_length=20, null=True, verbose_name='E2-1')),
                ('kategori_E2_2', models.CharField(blank=True, choices=[('3', '3')], max_length=20, null=True, verbose_name='E2-2')),
                ('kategori_F1_1', models.CharField(blank=True, choices=[('50', '50')], max_length=20, null=True, verbose_name='F1-1')),
                ('kategori_F2_1', models.CharField(blank=True, choices=[('20', '20')], max_length=20, null=True, verbose_name='F2-1')),
                ('kategori_F2_2', models.CharField(blank=True, choices=[('5', '5')], max_length=20, null=True, verbose_name='F2-2')),
                ('kategori_F3_1', models.CharField(blank=True, choices=[('20', '20')], max_length=20, null=True, verbose_name='F3-1')),
                ('kategori_F4_1', models.CharField(blank=True, choices=[('25', '25')], max_length=20, null=True, verbose_name='F4-1')),
                ('kategori_F4_2', models.CharField(blank=True, choices=[('15', '15')], max_length=20, null=True, verbose_name='F4-2')),
                ('kategori_F4_3', models.CharField(blank=True, choices=[('5', '5')], max_length=20, null=True, verbose_name='F4-3')),
                ('kategori_G1:(ATIFLAR)_1', models.CharField(blank=True, choices=[('3', '3')], max_length=20, null=True, verbose_name='G1:(ATIFLAR)-1')),
                ('kategori_G2_1', models.CharField(blank=True, choices=[('1', '1')], max_length=20, null=True, verbose_name='G2-1')),
                ('kategori_G3_1', models.CharField(blank=True, choices=[('1', '1')], max_length=20, null=True, verbose_name='G3-1')),
                ('kategori_G4_1', models.CharField(blank=True, choices=[('4', '4')], max_length=20, null=True, verbose_name='G4-1')),
                ('kategori_H1_1', models.CharField(blank=True, choices=[('4', '4')], max_length=20, null=True, verbose_name='H1-1')),
                ('kategori_H2_1', models.CharField(blank=True, choices=[('1/2', '1/2')], max_length=20, null=True, verbose_name='H2-1')),
                ('kategori_H3_1', models.CharField(blank=True, choices=[('3', '3')], max_length=20, null=True, verbose_name='H3-1')),
                ('kategori_H4_1', models.CharField(blank=True, choices=[('10/5', '10/5')], max_length=20, null=True, verbose_name='H4-1')),
            ],
        ),
    ]
