"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, IssueCreateView, IssueView, IssueUpdateView, IssueDeleteView, \
    StatusListView, StatusCreateView, StatusDeleteView, StatusUpdateView, TypeListView, TypeCreateView, \
    TypeDeleteView, TypeUpdateView, ProjectListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/update/<int:pk>', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>', IssueDeleteView.as_view(), name='issue_delete'),
    path('statuses/', StatusListView.as_view(), name='statuses'),
    path('status/create', StatusCreateView.as_view(), name='status_create'),
    path('status/update/<int:pk>', StatusUpdateView.as_view(), name='status_update'),
    path('status/delete/<int:pk>', StatusDeleteView.as_view(), name='status_delete'),
    path('types/', TypeListView.as_view(), name='types'),
    path('types/create', TypeCreateView.as_view(), name='type_create'),
    path('type/update/<int:pk>', TypeUpdateView.as_view(), name='type_update'),
    path('type/delete/<int:pk>', TypeDeleteView.as_view(), name='type_delete'),
    path('projects/', ProjectListView.as_view(), name='projects')

]
