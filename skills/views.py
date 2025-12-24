from django.shortcuts import render, get_object_or_404
from .models import Skill

# List of skills
def skill_list(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'skills/skill_list.html', context)

# Skill details page
def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    context = {'skill': skill}
    return render(request, 'skills/skill_details.html', context)
