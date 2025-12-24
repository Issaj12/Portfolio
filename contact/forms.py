from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'some@someone.com',
                'class': 'form-input'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '07******** (optional)',
                'class': 'form-input'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message',
                'class': 'form-textarea',
                'rows': 5
            }),
        }
