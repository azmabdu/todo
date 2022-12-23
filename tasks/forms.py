from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, page=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if page:
            self.fields['complete'].widget.attrs.update(
                {'class': 'complete'})

        else:
            self.fields['title'].widget.attrs.update(
                {'placeholder': 'Add new task...'})
