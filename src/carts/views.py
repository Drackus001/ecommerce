from django.shortcuts import render

# Create your views here.
def cart_home(request):
    cart_id = request.session.get('cart_id',None)
    if cart_id is None: # and isinstance(cart_id, int)
        print("Create new cart_id")
        request.session['cart_id'] = 12
    else:
        print('Cart_id is already exists')
    
    return render(request, 'carts/home.html', context=None)
    # print(request.session)
    # #print(dir(request.session))
    # # request.session.set_expiry(300) # 5 minutes
    # # request.session.session_key
    # # 'session_key', 'set_expiry'
    # key = request.session.session_key
    # #request.session['myname'] = 'Satyam Agarwal' # setting dummy session
    # request.session['card_id'] = 5
    # print(key)

    # return render(request, 'carts/home.html', context=None)