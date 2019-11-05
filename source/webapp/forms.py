from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Issue, Status, Type, Project


def get_all_project_of_user(user):
    return Project.objects.filter(teams__participant_id=user)


class IssueForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), label='Исполнитель', empty_label='Укажите исполнителя')

    class Meta:
        model = Issue
        exclude = ['created_at', 'created_by', 'project']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')