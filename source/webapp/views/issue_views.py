from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, QuerySet
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.models import Issue, Project
from webapp.forms import IssueForm, SimpleSearchForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.views.base_views import SearchView


def get_all_project_of_user(user):
    return Project.objects.filter(teams__participant_id=user)


class IndexView(SearchView):
    template_name = 'issue/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 4
    paginate_orphans = 0
    page_kwarg = 'page'
    ordering = ['-created_at']
    search_form = SimpleSearchForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['editable_projects'] = get_all_project_of_user(self.request.user)
        return context

    def get_filters(self):
        return Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)


class IssueView(DetailView):
    template_name = 'issue/issue.html'
    context_key = 'issue'
    model = Issue

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['editable_projects'] = get_all_project_of_user(self.request.user)
        return context

class IssueCreateView(CreateView):
    form_class = IssueForm
    model = Issue
    template_name = 'create.html'
    extra_context = {'title': 'Задачи'}

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields['project'].queryset = get_all_project_of_user(self.request.user)
        return form

    def form_valid(self, form):
        print()
        if form.cleaned_data['project'] in get_all_project_of_user(self.request.user):
            return super().form_valid(form)
        else:
            raise Http404('Вы не можете добавлять задачу в этот проект')


class IssueUpdateView(UserPassesTestMixin, UpdateView):
    form_class = IssueForm
    model = Issue
    template_name = 'update.html'
    extra_context = {'title': 'Задачи'}

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields['project'].queryset = get_all_project_of_user(self.request.user)
        return form

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().project in (get_all_project_of_user(self.request.user))


class IssueDeleteView(UserPassesTestMixin, DeleteView):
    model = Issue
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    extra_context = {'title': 'удалить Задачу'}

    def test_func(self):
        return self.get_object().project in get_all_project_of_user(self.request.user)
