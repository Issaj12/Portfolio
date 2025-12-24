from django import forms
from .models import CV
class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'content', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }