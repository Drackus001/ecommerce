from django.shortcuts import render

from .models import Cart

# Create your views here.

def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    
    return render(request, 'carts/home.html', context=None)
    
    
    #del request.session['cart_id']
    # print(request.session)
    # #print(dir(request.session))
    # # request.session.set_expiry(300) # 5 minutes
    # # request.session.session_key
    # # 'session_key', 'set_expiry'
    # key = request.session.session_key
    # #request.session['myname'] = 'Satyam Agarwal' # setting dummy session
    
