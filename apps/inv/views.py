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
