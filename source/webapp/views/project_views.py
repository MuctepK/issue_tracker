from django.urls import reverse, reverse_lazy
from webapp.models import Project
from django.views.generic import ListView, CreateView, DetailView, UpdateView
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