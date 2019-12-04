from django.shortcuts import render
from rest_framework import viewsets

from api_v1.serializers import IssueSerializer, ProjectSerializer
from webapp.models import Issue, Project


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()