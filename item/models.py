from django.db import models

# Create your models here.
class Item(models.Model):
    JENIS_OBAT= (
        ('Obat', 'Obat'),
        ('Suplemen', 'Suplemen')
    )
    image = models.CharField(max_length=255)
    nama = models.CharField(max_length=150)
    jenis = models.CharField(max_length=20, choices=JENIS_OBAT)
    deskripsi = models.TextField()
    khasiat = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)
    harga = models.IntegerField()
    satuan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama +', '+ self.jenis