from django import forms
from .models import PersonalData


class UserForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = ['name', 'nickname', 'email']
