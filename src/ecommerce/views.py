from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    # getting session 
    #print(request.session.get("myname",'unknown'))
    print(request.session.get('cart_id'))
    context = {
        'title' : 'Home',
        'content' : 'Welcome to Home Page'
    }
    return render(request, 'home_page.html', context=context)

def about_page(request):
    context = {
        'title' : 'About',
        'content' : 'Welcome to About Page'
    }
    return render(request, 'home_page.html', context=context)
    
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
      'title' : 'Contact',
      'content' : 'Welcome to Contact Page',
      "form" : contact_form,
    }
    if contact_form.is_valid():
          print(contact_form.cleaned_data)
    # if request.method == "POST":
    #       print(request.POST)
    #   print(request.POST.get('fullname'))
    #   print(request.POST.get('email'))
    #   print(request.POST.get('content'))
    return render(request, 'contact/view.html', context=context)

def logout_view(request):
    logout(request)
    return render(request, 'home_page.html', context=None)

def login_page(request):
      login_form = LoginForm(request.POST or None)
      context = {
        'form' : login_form,
      }
      
      if login_form.is_valid():
            usrname = request.POST.get('username')
            pswrd = request.POST.get('password')
            user = authenticate(username=usrname, password=pswrd)
            if user is not None:
                  if user.is_active:
                      #print(request.user.is_authenticated())
                      login(request,user)
                      print('user login')
                      print(login_form.cleaned_data)  
                      return redirect('/')
              
                  else:
                      print('User Account is disabled')
            else:
                print('Error message: User Account not found!')
     
      return render(request,'auth/login.html', context=context)


User = get_user_model()
def register_page(request):
      form = RegisterForm(request.POST or None)
      context = {
        'form':form
      }
      #username = request.POST.get('username')
      
      #print(nuser)
      if form.is_valid():
            uname = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user = User.objects.create_user(
              username=uname,
              email=email,
              password=password)            
            print(new_user)
            print(form.cleaned_data)
      return render(request, 'auth/register.html',context=context)


def old_home_page(request):
    html_ = """
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
  <div class="text-center">
    <h1>Hello, world!</h1>
</div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
    """
    return HttpResponse(html_)