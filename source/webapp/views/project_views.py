from django.urls import reverse, reverse_lazy
from webapp.models import Project
from django.views.generic import ListView


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    paginate_by = 3
    paginate_orphans = 0
    page_kwarg = 'page'
    ordering = ['-created_at']