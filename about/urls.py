from django.urls import path
from . import views

urlpatterns = [

 path('education/', views.about_education, name='about'),
    path('services/', views.about_services, name='about_services'),
    path('testimonials/', views.about_testimonials, name='about_testimonials'),
    path('testimonials/<int:testimonial_id>/', views.testimonial_detail, name='testimonial_detail'),

]