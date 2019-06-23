from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL
from products.models import Product

class CartManager(models.Manager):
    
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id',None)
        qs = self.get_queryset().filter(id=cart_id)

        if qs.count() == 1:    
            new_obj = False        
            cart_obj = qs.first()
            if request.user.is_active and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()     
        else:
            new_obj = True
            cart_obj = Cart.objects.new(user=request.user)
            request.session['cart_id'] = cart_obj.id

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