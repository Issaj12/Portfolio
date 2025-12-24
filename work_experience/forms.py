from  django import forms
from .models import WorkExperience

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company_photo', 'company_name', 'position', 'start_date', 'end_date', 'description']
        widgets = {
            'company_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }