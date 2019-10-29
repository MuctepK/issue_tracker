from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.models import Issue
from webapp.forms import IssueForm, SimpleSearchForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.views.base_views import SearchView


class IndexView(SearchView):
    template_name = 'issue/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 4
    paginate_orphans = 0
    page_kwarg = 'page'
    ordering = ['-created_at']
    search_form = SimpleSearchForm

    def get_filters(self):
        return Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_key = 'issue'
    model = Issue


class IssueCreateView(LoginRequiredMixin,CreateView):
    form_class = IssueForm
    model = Issue
    template_name = 'create.html'
    extra_context = {'title': 'Задачи'}

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    form_class = IssueForm
    model = Issue
    template_name = 'update.html'
    extra_context = {'title': 'Задачи'}

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    extra_context = {'title': 'удалить Задачу'}
