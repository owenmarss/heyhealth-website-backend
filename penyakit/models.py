from django.db import models

# Create your models here.
class Penyakit(models.Model):
    nama = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    deskripsi = models.TextField()
    penyebab = models.TextField(default='')
    gejala = models.TextField()
    pencegahan = models.TextField()
    pengobatan = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        ordering=('nama', )