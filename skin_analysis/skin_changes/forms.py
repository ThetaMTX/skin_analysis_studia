from django import forms
from .models import SkinChange


class SkinChangeForm(forms.ModelForm):
    class Meta:
        model = SkinChange
        fields = ['image', 'description']
