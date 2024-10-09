from django.db import models
from operator import mod
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class OrderSatatus(models.TextChoices):
    PROCESSED = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'

class PaymentSatatus(models.TextChoices):
    PAID = 'paid'
    UNPAID = 'unpaid'

class PaymentMethod(models.TextChoices):
    COD = 'cod'
    CARD = 'card'

    
class Order(models.Model):
    city = models.CharField(blank=False, default="" , max_length=400)
    zip_code = models.CharField( max_length=100, blank=False, default="")
    street = models.CharField( max_length=500, blank=False, default="")
    state = models.CharField( max_length=100, blank=False, default="")
    country = models.CharField( max_length=100, blank=False, default="")
    phone = models.CharField( max_length=100, blank=False, default="")
    total_amount = models.models.IntegerField( default=0)
    payment_status = models.CharField(max_length=50, choices=PaymentSatatus.choices, default=PaymentSatatus.UNPAID)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices, default=PaymentMethod.COD)
    status = models.CharField(max_length=50, choices=OrderSatatus.choices, default=OrderSatatus.PROCESSED)
    user = models.ForeignKey(User, null= True, on_delete=models.SET_NULL)
    created_on = models.DateField( auto_now_add=True)

    def __str__(self):
        return str(self.id)