from django.db.models import ProtectedError
from django.shortcuts import render
from django.urls import reverse_lazy

from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView
from webapp.views.base_views import UpdateView, DeleteView


class StatusListView(ListView):
    model = Status
    template_name = 'status/status_index.html'


class StatusCreateView(CreateView):
    template_name = 'create.html'
    extra_context = {'title': 'Статуса'}
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')


class StatusUpdateView(UpdateView):
    template_name = 'update.html'
    extra_context = {'title': 'Статуса'}
    model = Status
    form_class = StatusForm
    redirect_url = reverse_lazy('statuses')


class StatusDeleteView(DeleteView):
    template_name = 'delete.html'
    extra_context = {'title': 'Статус'}
    model = Status
    redirect_url = reverse_lazy('statuses')
    failure_template_name = 'partial/error.html'
