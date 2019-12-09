from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api_v1.serializers import IssueSerializer, ProjectSerializer
from webapp.models import Issue, Project, Team
from rest_framework.permissions import SAFE_METHODS, AllowAny, \
    DjangoModelPermissions
from rest_framework.exceptions import PermissionDenied, APIException


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [DjangoModelPermissions]

    def get_permissions(self):
        print(self.kwargs.get('pk'))
        if self.request.method in SAFE_METHODS:
            return []
        else:
            if self.is_part_of_project(self.kwargs.get('pk'),self.request.user):
                return super().get_permissions()
            else:
                raise  PermissionDenied({"detail":"You don't have permission to do this."
                                                  "You are not part of the project'"})

    def get_all_project_of_user(self, user):
        return Project.objects.filter(teams__participant_id=user)

    def is_part_of_project(self, issue_pk, user):
        return self.get_project_of_issue(issue_pk) in self.get_all_project_of_user(user)

    def get_project_of_issue(self,pk):
        if pk:
            print(Issue.objects.get(pk=pk).project, self.get_all_project_of_user(self.request.user))
            return Issue.objects.get(pk=pk).project
        else:
            try:
                return Project.objects.get(pk=self.request.data['project'])
            except ObjectDoesNotExist:
                raise APIException(detail =  "Specified project does not exist", code = status.HTTP_404_NOT_FOUND)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [DjangoModelPermissions]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        else:
            return super().get_permissions()