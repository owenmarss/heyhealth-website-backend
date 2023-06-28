from django.db import models
from account.models import User
from dokter.models import Dokter

# Create your models here.
class Janji(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Dokter, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    keluhan = models.TextField()

    def __str__(self):
        return self.dokter.nama +', '+ self.date +', '+ self.time