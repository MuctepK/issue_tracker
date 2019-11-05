from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.urls import reverse, reverse_lazy


from webapp.models import Issue, Project
from webapp.forms import IssueForm, SimpleSearchForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.views.base_views import SearchView


def get_all_project_of_user(user):
    return Project.objects.filter(teams__participant_id=user)


def get_all_teammates_of_user(user):
    return User.objects.filter(teams__project__in=get_all_project_of_user(user)).exclude(id=user.id)


def get_participants_of_project(project,user):
    return User.objects.filter(teams__project=project).exclude(id=user.id)


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
        if self.request.user.is_authenticated:
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
        context['can_edit'] = self.request.user.is_authenticated and \
                              self.object.project in get_all_project_of_user(self.request.user)
        return context


class IssueCreateView(LoginRequiredMixin, CreateView):
    form_class = IssueForm
    model = Issue
    template_name = 'create.html'
    extra_context = {'title': 'Задачи'}

    def get_success_url(self):
        return reverse('webapp:issue_view', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields['project'].queryset = get_all_project_of_user(self.request.user)
        form.fields['assigned_to'].queryset = get_all_teammates_of_user(self.request.user)
        return form

    def form_valid(self, form):
        print(get_all_project_of_user(form.cleaned_data['assigned_to']))

        if not (form.cleaned_data['project'] in get_all_project_of_user(self.request.user)):
            raise Http404('Вы не можете добавлять задачу в этот проект')
        else:
            self.object = form.save(commit=False)
            self.object.created_by = self.request.user
            return super().form_valid(form)


class IssueUpdateView(UserPassesTestMixin, UpdateView):
    form_class = IssueForm
    model = Issue
    template_name = 'update.html'
    extra_context = {'title': 'Задачи'}

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields['project'].queryset = get_all_project_of_user(self.request.user)
        form.fields['assigned_to'].queryset = get_participants_of_project(self.object.project, self.request.user)
        return form

    def form_valid(self, form):
        if self.get_object().project != form.cleaned_data['project']:
            raise Http404("Нельзя менять проект уже созданной задачи!")
        return super().form_valid(form)

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
