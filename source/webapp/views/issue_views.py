from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Issue
from webapp.forms import IssueForm
from django.views.generic import TemplateView, ListView, CreateView
from django.views import View
from .base_views import DetailView


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


class IssueCreateView(View):

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'create.html', context={'form': form,
                                                       'title': 'Задачи'})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type = form.cleaned_data['type']
            )
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'create.html', context={'form': form,
                                                           'title': 'Задачи'})


class IssueUpdateView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id,

        })
        return render(request, 'update.html', context={'form': form,
                                                       'issue': issue,
                                                       'title': 'Задачи'})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type = form.cleaned_data['type']
            )
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'update.html', context={'form': form,
                                                           'issue': issue,
                                                           'title': 'Задачи'})


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