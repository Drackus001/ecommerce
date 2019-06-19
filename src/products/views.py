from django.http import Http404
from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

class ProductListView(ListView): # class based listview
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request): # function based listview
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, "products/list.html", context=context)



# Detailview example
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Doesn't Exist")
        return instance
    
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
#****
    #instance = get_object_or_404(Product,pk=pk)
    #queryset = Product.objects.all()
    
    #try:
     #   instance = Product.objects.get(id=pk)
    #except Product.DoesNotExist:
     #   print('no matching product found')
      #  raise Http404("Product Doesn't Exist")
    #except:
     #   print('huh?')
#****
    # qs = Product.objects.filter(id=pk)
    # print(qs)
    # if qs.count() == 1 and qs.exists():
    #     instance = qs.first()
    # else:
    #     raise Http404("Product not found")

#****
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product not found!")
#****

    context = {
        'object':instance
    }
    return render(request, "products/detail.html", context=context)