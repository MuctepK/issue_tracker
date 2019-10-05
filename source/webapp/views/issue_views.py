from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Issue
from webapp.forms import IssueForm
from django.views.generic import TemplateView, ListView, CreateView
from django.views import View
from .base_views import DetailView, UpdateView


class IndexView(ListView):
    template_name = 'issue/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 3
    paginate_orphans = 0
    page_kwarg = 'page'


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

    def get_redirect_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'delete.html', context={'object': issue,
                                                       'title': 'Задачу'})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')