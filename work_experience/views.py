from django.shortcuts import render, get_object_or_404
from work_experience.models import WorkExperience
from django.shortcuts import render

# Create your views here.
def work_list(request):
    works = WorkExperience.objects.all().order_by('-start_date')
    context =  {'works': works}
    return render(request, 'work/work_list.html',context)

def work_detail(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk)
    context = {'work': work}
    return render(request, 'work/work_detail.html', context)



