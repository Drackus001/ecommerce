from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart

# Create your views here.

def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj 
    }
    
    return render(request, 'carts/home.html', context=context)


def cart_update(request):
    print(request.POST.get('product_id')) 
    product_id = request.POST.get('product_id')
    #request.POST.get('product_id')
#   print(Product.objects.get(id=1))
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("show message to user ,Product is gone")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        # add_button = request.POST.get('add_button')
        # remove_button = request.POST.get('remove_button')



        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)    
        else:    
            cart_obj.products.add(product_obj)
    request.session['cart_items'] = cart_obj.products.count()
            
#    return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")



    # product_id = 1
    # product_obj = Product.objects.get(id=product_id)
    # cart_obj, new_obj = Cart.objects.new_or_get(request)
    # if product_obj in cart_obj.products.all():
    #     cart_obj.products.remove(product_obj)
    # else:  
    #     cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
    # # cart_obj.products.remove(product_obj)
    # #return redirect(product_obj.get_absolute_url())
    # return redirect("cart:home")

    #del request.session['cart_id']
    # print(request.session)
    # #print(dir(request.session))
    # # request.session.set_expiry(300) # 5 minutes
    # # request.session.session_key
    # # 'session_key', 'set_expiry'
    # key = request.session.session_key
    # #request.session['myname'] = 'Satyam Agarwal' # setting dummy session

