# Generated by Django 4.2 on 2023-04-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('nama_item', models.CharField(max_length=255)),
                ('alamat', models.TextField()),
                ('nomor_telepon', models.CharField(max_length=20)),
                ('pembayaran', models.CharField(choices=[('Mobile BCA', 'Mobile BCA'), ('GoPay', 'GoPay'), ('ShopeePay', 'ShopeePay'), ('OVO', 'OVO'), ('COD', 'COD')], max_length=50)),
            ],
        ),
    ]
