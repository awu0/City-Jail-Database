from django import forms
from django.forms import ModelForm

from jail.models import Criminal


class CriminalForm(ModelForm):
    class Meta:
        model = Criminal
        fields = [
            'first_name',
            'last_name',
            'street',
            'city',
            'state',
            'zip',
            'phone',
            'v_status',
            'p_status'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'v_status': forms.TextInput(attrs={'class': 'form-control'}),
            'p_status': forms.TextInput(attrs={'class': 'form-control'})
        }
