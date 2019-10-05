from django.db.models import ProtectedError
from django.shortcuts import render
from django.urls import reverse_lazy

from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import ListView, CreateView
from webapp.views.base_views import UpdateView, DeleteView


class TypeListView(ListView):
    model = Type
    template_name = 'type/type_index.html'


class TypeCreateView(CreateView):
    template_name = 'create.html'
    extra_context = {'title': 'Типа'}
    model = Type
    form_class = TypeForm
    success_url = reverse_lazy('types')


class TypeUpdateView(UpdateView):
    template_name = 'update.html'
    extra_context = {'title': 'Типа'}
    model = Type
    form_class = TypeForm
    redirect_url = reverse_lazy('types')


class TypeDeleteView(DeleteView):
    extra_context = {'title': 'Тип'}
    template_name = 'delete.html'
    model = Type
    redirect_url = reverse_lazy('types')

