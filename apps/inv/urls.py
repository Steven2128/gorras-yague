# Django
from django.urls import path
# Views
from .views import *

urlpatterns = [
    path('create/', PQRCreateView.as_view(), name='pqr_index'),
    path('', PQRListView.as_view(), name='pqr_list'),
]