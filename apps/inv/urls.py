# Django
from django.urls import path
# Views
from .views import *

urlpatterns = [
    path('pqr/create/', PQRCreateView.as_view(), name='pqr_create'),
    path('pqrs/', PQRListView.as_view(), name='pqr_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
]