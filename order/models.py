from django.db import models
from account.models import User
from item.models import Item

# Create your models here.
class Order(models.Model):
    METODE_PEMBAYARAN = (
        ('Mobile BCA', 'Mobile BCA'),
        ('GoPay', 'GoPay'),
        ('ShopeePay', 'ShopeePay'),
        ('OVO', 'OVO'),
        ('COD', 'COD')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)
    quantities = models.CharField(max_length=255)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=20)
    pembayaran = models.CharField(max_length=50, choices=METODE_PEMBAYARAN)