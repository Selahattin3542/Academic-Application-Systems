# Generated by Django 4.1.7 on 2023-07-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('bastarih', models.DateField()),
                ('bittar', models.DateField()),
                ('aciklama', models.TextField()),
            ],
        ),
    ]
