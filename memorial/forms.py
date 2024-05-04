from django import forms
from .models import Memorial

class MemorialForm(forms.ModelForm):
    class Meta:
        model = Memorial
        fields = '__all__'

               