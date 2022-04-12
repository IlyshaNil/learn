from django.shortcuts import render
from .models import Project, Technology

def index(request):
    projects = Project.objects.all()
    stack = Technology.objects.all()
    return render(request, 'index.html', {'projects': projects, 'stack': stack})


def experience(request):
    return render(request, 'about.html')