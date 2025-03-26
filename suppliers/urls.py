from django.urls import path

from .views import SupplierListView, SupplierCreateView, SupplierDetailView, SupplierUpdateView, SupplierDeleteView, SupplierCreateListAPIView, SupplierRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('Suppliers/list/', SupplierListView.as_view(), name='supplier_list'),
    path('Suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('Suppliers/<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('Suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('Suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
    
    
    path('api/v1/suppliers/', SupplierCreateListAPIView.as_view(), name='supplier-create-list-api-view'),
    path('api/v1/suppliers/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail-api-view'),
]