from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description', 'picture', 'acquired_from']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
