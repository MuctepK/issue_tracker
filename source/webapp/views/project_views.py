from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy
from webapp.models import Project, PROJECT_DEFAULT_STATUS
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import ProjectForm


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    paginate_by = 3
    paginate_orphans = 0
    page_kwarg = 'page'
    ordering = ['-created_at']


class ProjectDetailView(DetailView):
    template_name = 'project/project.html'
    context_key = 'project'
    model = Project

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == 'closed':
            raise Http404('Указанный проект не найден...')
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-created_at')
        self.paginate_comments_to_context(issues, context)
        return context

    def paginate_comments_to_context(self, issues, context):
        paginator = Paginator(issues, 2, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['issues'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'create.html'
    extra_context = {'title': 'Проекта'}
    success_url = reverse_lazy('projects')


class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'update.html'
    extra_context = {'title': 'Проекта'}

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'delete.html'
    success_url = reverse_lazy('projects')
    extra_context = {'title': 'закрыть Проект'}

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 'closed'
        self.object.save()
        return HttpResponseRedirect(success_url)
