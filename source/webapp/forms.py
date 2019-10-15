from django import forms
from django.forms import widgets
from webapp.models import Issue, Status, Type, Project


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['created_at']


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