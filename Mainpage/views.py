from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from contact.models import Contact
from skills.models import Skill
from skills.forms import SkillForm
from work_experience.models import WorkExperience
from work_experience.forms import WorkExperienceForm
from about.models import Education, Service, Testimonial
from about.forms import EducationForm, ServiceForm, TestimonialForm
from CVs.models import CV
from CVs.forms import CVForm
from django.contrib.auth.decorators import login_required
import csv




# Main page view
def Main(request):
    return render(request, 'Main/mainpage.html')


# Admin dashboard: contacts + skills
@login_required
def admin_dashboard(request):
    contacts = Contact.objects.all().order_by('-submitted_at')
    skills = Skill.objects.all()
    works = WorkExperience.objects.all()
    educations = Education.objects.all().order_by('-start_year')  # <-- fixed line
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    work_count = WorkExperience.objects.count()
    education_count = Education.objects.count()
    service_count = Service.objects.count()
    testimonial_count = Testimonial.objects.count()
    cvs = CV.objects.all().order_by('-created_at')

    # Handle contact actions
    if 'download_csv' in request.GET:
        return download_contacts_csv(contacts)
    if 'clear_all' in request.GET:
        contacts.delete()
        return redirect('admin_dashboard')
    if 'delete' in request.GET:
        contact_id = request.GET.get('delete')
        Contact.objects.filter(id=contact_id).delete()
        return redirect('admin_dashboard')



    context = {
        'contacts': contacts,
        'skills': skills,
        'works': works,
        'educations': educations,
        'services': services,
        'testimonials': testimonials,
        'work_count': work_count,
        'education_count': education_count,
        'service_count': service_count,
        'testimonial_count': testimonial_count,
        'cvs': cvs,
    }
    return render(request, 'Main/admin_dashboard.html', context)


# CSV download for contacts
def download_contacts_csv(contacts):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Message', 'Submitted At'])
    for c in contacts:
        writer.writerow([c.name, c.email, c.phone, c.message, c.submitted_at])
    return response


# Admin dashboard: create skill
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill created successfully.')
            return redirect('admin_dashboard')
    else:
        form = SkillForm()
    context = {'form': form, 'title': 'Create Skill'}
    return render(request, 'skills/skill_form.html', context)


# Admin dashboard: update skill
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully.')
            return redirect('admin_dashboard')
    else:
        form = SkillForm(instance=skill)
    context = {'form': form, 'title': 'Update Skill'}
    return render(request, 'skills/skill_form.html', context)


# Admin dashboard: delete skill
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully.')
        return redirect('admin_dashboard')
    context = {'skill': skill}
    return render(request, 'skills/skill_delete.html', context)


# work experience crud operations



def work_create(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = WorkExperienceForm()
    context = {'form': form}
    return render(request, 'work/form.html', context)


def work_update(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = WorkExperienceForm(instance=work)
    context = {'form': form}
    return render(request, 'work/form.html', context)



def work_delete(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk)
    if request.method == 'POST':
        work.delete()
        return redirect('admin_dashboard')
    context = {'work': work}
    return render(request, 'work/delete.html', context)


# about/views.py



# ------------------
# Education CRUD
# ------------------

def education_create(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    context = {'form': form,
               'title': 'Add Education'}
    return render(request, 'about/form.html', context)


def education_update(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST or None, instance=edu)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    context = {'form': form,
               'title': 'Edit Education'}

    return render(request, 'about/form.html', context)


def education_delete(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        edu.delete()
        return redirect('admin_dashboard')
    context = {'object': edu,
               'title': 'Delete Education'}
    return render(request, 'about/delete.html', context)

# ------------------
# Service CRUD
# ------------------

def service_create(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    context = {'form': form,
                'title': 'Add Service'}
    return render(request, 'about/form.html', context)


def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    context = {'form': form,
               'title': 'Edit Service'}
    return render(request, 'about/form.html', context)


def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('admin_dashboard')
    context =  {'object': service,
                'title': 'Delete Service'}
    return render(request, 'about/delete.html',context)

# ------------------
# Testimonial CRUD
# ------------------

def testimonial_create(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.user.is_staff:  # or use is_superuser if only superusers are admins
                return redirect('admin_dashboard')
            else:
                return redirect('about_testimonials')
    else:
        form = TestimonialForm()
    context = {'form': form, 'title': 'Add Testimonial'}
    return render(request, 'about/form.html', context)


def testimonial_update(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TestimonialForm(instance=testimonial)
    context = {'form': form, 'title': 'Edit Testimonial'}
    return render(request, 'about/form.html', context)


def testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('admin_dashboard')
    context = {'object': testimonial,
               'title': 'Delete Testimonial'}
    return render(request, 'about/delete.html', context)



# ================
# CV CRUD Operations
# ================

# Create a new CV
def cv_create(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV created successfully!')
            return redirect('admin_dashboard')
    else:
        form = CVForm()
    context = {'form': form,
               'title': 'Add CV'}
    return render(request, 'CV/cv_form.html', context)

# Update an existing CV
def cv_update(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = CVForm(instance=cv)
    context = {'form': form,
               'title': 'Edit CV'}
    return render(request, 'CV/cv_form.html', context)

# Delete a CV
def cv_delete(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == 'POST':
        cv.delete()
        messages.success(request, 'CV deleted successfully!')
        return redirect('admin_dashboard')
    context = {'cv': cv,
               'title': 'Delete CV'}
    return render(request, 'CV/cv_delete.html', context)
