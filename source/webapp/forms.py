from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=200, label='Заголовок', required=True)
    description = forms.CharField(max_length=3000, label='Текст', required=False,
                           widget=widgets.Textarea(attrs={'rows': 8, 'cols': 15}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус',
                                      empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Тип задачи',
                                    empty_label=None)

