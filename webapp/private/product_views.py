from django.views.generic import ListView, CreateView
from webapp.models.product import Product
from django.core.urlresolvers import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'private/product/list.html'
    context_object_name = 'products'


class ProductNewView(CreateView):
    model = Product
    template_name = 'private/product/create.html'
    success_url = reverse_lazy('product_list')

