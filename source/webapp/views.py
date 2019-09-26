from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from webapp.models import Issue, Status, Type
from webapp.forms import IssueForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views import View


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=pk)
        return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'create.html', context={'form': form})

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
            return render(request, 'create.html', context={'form': form})


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
                                                       'issue': issue})

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
                                                           'issue': issue})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'delete.html', context={'object': issue})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')


class StatusListView(ListView):
    model = Status
    template_name = 'status_list.html'


class StatusCreateView(CreateView):
    template_name = 'create.html'
    model = Status
    fields = ['name']
    success_url = reverse_lazy('statuses')


class StatusUpdateView(UpdateView):
    template_name = 'update.html'
    model = Status
    fields = ['name']
    success_url = reverse_lazy('statuses')


class StatusDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Status
    success_url = reverse_lazy('statuses')

