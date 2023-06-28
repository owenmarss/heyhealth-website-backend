# Generated by Django 4.2 on 2023-04-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=200)),
                ('bidang', models.CharField(max_length=255)),
                ('usia', models.IntegerField()),
                ('pengalaman', models.IntegerField()),
                ('lokasi_praktek', models.CharField(max_length=255)),
                ('jam_praktek', models.CharField(max_length=200)),
            ],
        ),
    ]
