from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Issue, Status, Type, Project


def get_all_project_of_user(user):
    return Project.objects.filter(teams__participant_id=user)


class IssueForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),label='К проекту',empty_label='Выберите проект')
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), label='Исполнитель', empty_label='Укажите исполнителя')

    class Meta:
        model = Issue
        exclude = ['created_at', 'created_by']
    def clean_assigned_to(self):
        assigned_to = self.cleaned_data['assigned_to']
        project = self.cleaned_data['project']
        if not (project in get_all_project_of_user(assigned_to)):
            raise ValidationError('Исполнитель не принадлежит этому проекту', code ='not_part_of_project')


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