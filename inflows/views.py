from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Inflow
from .forms import InflowForm
from . import serializers


class InflowListView(LoginRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset
    

class InflowCreateView(LoginRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'
    
    

class InflowDetailView(LoginRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'
    
    
    
class InflowCreateListAPIView(generics.ListCreateAPIView): # Criando a API
    queryset = Inflow.objects.all()
    serializer_class = serializers.InflowSerializer
    
    
class InflowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = serializers.InflowSerializer