from django.shortcuts import render

from .models import Cart

# Create your views here.
def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New cart created.')
    return cart_obj

def cart_home(request):
    request.session['cart_id'] = "21"
    cart_id = request.session.get('cart_id',None)
    qs = Cart.objects.filter(id=cart_id)

    if qs.count() == 1:     # and isinstance(cart_id, int)
        print('cart_id already exists!')
        cart_obj = Cart.objects.create(user=None)
        cart_obj = qs.first()
        if request.user.is_active and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
               
    else:
        cart_obj = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id
    return render(request, 'carts/home.html', context=None)
    
    
    #del request.session['cart_id']
    # print(request.session)
    # #print(dir(request.session))
    # # request.session.set_expiry(300) # 5 minutes
    # # request.session.session_key
    # # 'session_key', 'set_expiry'
    # key = request.session.session_key
    # #request.session['myname'] = 'Satyam Agarwal' # setting dummy session
    
