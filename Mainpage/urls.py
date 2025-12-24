from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Main, name='Home'),
    path('adm/', views.admin_dashboard, name='admin_dashboard'),  
    

    path('login/', auth_views.LoginView.as_view(template_name='Main/login.html'), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),

  # admin dashboard CRUD

    path('dashboard/create/', views.skill_create, name='skill_create'),
    path('dashboard/<int:pk>/update/', views.skill_update, name='skill_update'),
    path('dashboard/<int:pk>/delete/', views.skill_delete, name='skill_delete'),

        # Admin dashboard (CRUD)
    path('create/', views.work_create, name='work_create'),
    path('edit/<int:pk>/', views.work_update, name='work_update'),
    path('delete/<int:pk>/', views.work_delete, name='work_delete'),


# about page
  # Admin CRUD for Education
    path('education/add/', views.education_create, name='education_create'),
    path('education/<int:pk>/update/', views.education_update, name='education_update'),
    path('education/<int:pk>/delete/', views.education_delete, name='education_delete'),

    # Admin CRUD for Services
    path('services/add/', views.service_create, name='service_create'),
    path('services/<int:pk>/update/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Admin CRUD for Testimonials
    path('testimonials/add/', views.testimonial_create, name='testimonial_create'),
    path('testimonials/<int:pk>/update/', views.testimonial_update, name='testimonial_update'),
    path('testimonials/<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),

# admin crud function of CVs
    path('add/', views.cv_create, name='cv_create'),
    path('<int:pk>/edit/', views.cv_update, name='cv_update'),
    path('<int:pk>/delete/', views.cv_delete, name='cv_delete'),
]