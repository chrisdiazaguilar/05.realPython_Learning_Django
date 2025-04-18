from django.shortcuts import render
from projects.models import Project

# Create your views here.


def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'all_projects.html')
    print(projects)
    return render(request, 'all_projects.html', {'projects': projects})
