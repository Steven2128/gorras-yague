# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
# Forms
from apps.inv.forms import *
# Models
from apps.inv.models import *


class PQRCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """PQR Create View"""
    model = PQR
    template_name = 'inv/PQRForm.html'
    form_class = PQRForm
    success_message = 'Solicitud creada exitosamente!'
    success_url = reverse_lazy('pqr_list')


class PQRListView(SuccessMessageMixin, LoginRequiredMixin, ListView):
    """PQR List View"""
    model = PQR
    context_object_name = 'pqrs'
    template_name = 'inv/PQRList.html'


class ProductListView(SuccessMessageMixin, LoginRequiredMixin, ListView):
    """Product List View"""
    model = Product
    context_object_name = 'products'
    template_name = 'inv/productList.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        size_filter = self.request.GET.get('size')  # Obtener el valor del parámetro "size" de la URL
        if size_filter:
            queryset = queryset.filter(size=size_filter)

        return queryset


class ProductCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Product Create View"""
    model = Product
    template_name = 'inv/productForm.html'
    form_class = ProductForm
    success_message = 'Producto creado exitosamente!'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        category = Category.objects.get(id=1)
        form.instance.category = category

        return super().form_valid(form)
