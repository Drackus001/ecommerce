from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL
from products.models import Product

class CartManager(models.Manager):
    def new(self,user=None):
        user_obj = None
        if user is not None:
            if user.is_active:
                user_obj = user
        return self.model.objects.create(user= user_obj)

class Cart(models.Model):
    user        = models.ForeignKey(User,blank=True, null=True,on_delete=True)
    products    = models.ManyToManyField(Product,blank=True)
    total       = models.DecimalField(decimal_places=2,default=0.00,max_digits=100)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects     = CartManager()

    def __str__(self):
        return str(self.id)