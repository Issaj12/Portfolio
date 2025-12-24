from django import forms
from .models import Education, Service, Testimonial

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
