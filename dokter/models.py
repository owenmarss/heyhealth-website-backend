from django.db import models
from rumah_sakit.models import Rs

# Create your models here.
class Dokter(models.Model) :
    image = models.CharField(max_length=255)
    nama = models.CharField(max_length=200)
    bidang = models.CharField(max_length=255)
    usia = models.IntegerField()
    pengalaman = models.IntegerField()
    lokasi_praktek = models.OneToOneField(Rs, on_delete=models.CASCADE)
    jam_praktek = models.CharField(max_length=200)

    def __str__(self):
        return self.nama