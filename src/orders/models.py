from django.db import models

from carts.models import Cart
# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=120)
    #billing_profile
    #shipphing_address
    #billing address
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, default='created')