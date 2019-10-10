from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.models import Issue
from webapp.forms import IssueForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView


class IndexView(ListView):
    template_name = 'issue/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 3
    paginate_orphans = 0
    page_kwarg = 'page'
    ordering = ['-created_at']


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_key = 'issue'
    model = Issue


class IssueCreateView(CreateView):
    form_class = IssueForm
    model = Issue
    template_name = 'create.html'
    extra_context = {'title': 'Задачи'}

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(UpdateView):
    form_class = IssueForm
    model = Issue
    template_name = 'update.html'
    extra_context = {'title': 'Задачи'}

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
    extra_context = {'title': 'удалить Задачу'}
