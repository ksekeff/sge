from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from . import models, forms, serializers
from .models import Product
from categories.models import Category
from brands.models import Brand



class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products' # Nome usado no template
    paginate_by = 10
    permission_required = 'products.view_product'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        series_number = self.request.GET.get('series_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if series_number:
            queryset = queryset.filter(series_number__icontains=series_number)
        if category:
            queryset = queryset.filter(category_id=category)
        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context
    
    


class ProductCreateView(LoginRequiredMixin,  PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'
    
    
class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    model = Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'
    
    

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'

    
class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'
  
    
class ProductCreateListAPIView(generics.ListCreateAPIView): # Criando a API
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer