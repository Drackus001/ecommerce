from products.models import Product
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class SearchProductView(ListView): 
   
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
        

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        print(method_dict)
        query = method_dict.get('q', None) #shirt is default # method_dict['q'] will raise error if q is not set (so that's why use get())
        print(method_dict)
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.all()

        '''
        __iconatins = field contains this
        __iexact = field is exactly this
        '''
       

        