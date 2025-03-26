from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView, OutflowCreateListAPIView, OutflowRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('outflow/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflow/create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('outflow/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),
    
    
    path('api/v1/outflows/', OutflowCreateListAPIView.as_view(), name='outflow-create-list-api-view'),
    path('api/v1/outflow/<int:pk>/', OutflowRetrieveUpdateDestroyAPIView.as_view(), name='outflow-detail-api-view'),
]