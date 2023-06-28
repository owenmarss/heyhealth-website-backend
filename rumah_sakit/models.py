from django.db import models

# Create your models here.
class Rs(models.Model) :
    DAERAH = (
        ('Jakarta Utara', 'Jakarta Utara'),
        ('Jakarta Selatan', 'Jakarta Selatan'),
        ('Jakarta Pusat', 'Jakarta Pusat'),
        ('Jakarta Barat', 'Jakarta Barat'),
        ('Jakarta Timur', 'Jakarta Timur')
    )

    image = models.CharField(max_length=255)
    nama = models.CharField(max_length=200)
    alamat = models.TextField()
    daerah = models.CharField(max_length=100, choices=DAERAH)
    no_telepon = models.CharField(max_length=25)
    deskripsi = models.TextField()
    fasilitas = models.TextField()

    def __str__(self):
        return self.nama +', '+ self.daerah