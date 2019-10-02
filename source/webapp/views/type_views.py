from django.db.models import ProtectedError
from django.shortcuts import render
from django.urls import reverse_lazy
from webapp.models import Type
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class TypeListView(ListView):
    model = Type
    template_name = 'type/type_index.html'


class TypeCreateView(CreateView):
    template_name = 'create.html'
    extra_context = {'title': 'Типа'}
    model = Type
    fields = ['name']
    success_url = reverse_lazy('types')


class TypeUpdateView(UpdateView):
    template_name = 'update.html'
    extra_context = {'title': 'Типа'}
    model = Type
    fields = ['name']
    success_url = reverse_lazy('types')


class TypeDeleteView(DeleteView):
    extra_context = {'title': 'Тип'}
    template_name = 'delete.html'
    model = Type
    success_url = reverse_lazy('types')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'partial/error.html')