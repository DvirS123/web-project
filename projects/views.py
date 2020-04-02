from django.shortcuts import render

from .models import Project

def projects(request):
	projects = Project.objects
	return render(request, 'project/projects.html', {'projects':projects})