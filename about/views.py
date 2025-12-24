# about/views.py
from django.shortcuts import render,  get_object_or_404
from .models import Education, Service, Testimonial
from CVs.models import CV  


def about_education(request):
    education_list = Education.objects.all()
    return render(request, 'about/about.html', {
        'section': 'education',
        'education_list': education_list
    })

def about_services(request):
    services = Service.objects.all()
    return render(request, 'about/about.html', {
        'section': 'services',
        'services': services
    })

def about_testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'about/about.html', {
        'section': 'testimonials',
        'testimonials': testimonials
    })

def testimonial_detail(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)
    return render(request, 'about/testimonial.html', {
        'testimonial': testimonial
    })

def about_cvs(request):
    cvs = CV.objects.all().order_by('-created_at')
    return render(request, 'about/about.html', {
        'section': 'cvs',
        'cvs': cvs
    })

def cv_detail(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)
    return render(request, 'CV/cv_detail.html', {
        'cv': cv
    })
