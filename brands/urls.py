from django.urls import path

from .views import BrandListView

urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brands_list'),  
]