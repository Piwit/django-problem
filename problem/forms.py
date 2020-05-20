from django import forms

from .models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ['resolved', 'resolved_at']
