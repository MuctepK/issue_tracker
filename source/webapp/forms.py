from django import forms
from django.forms import widgets
from webapp.models import Issue, Status, Type


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['created_at']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
