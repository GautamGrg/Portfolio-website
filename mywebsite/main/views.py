from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home (request):
    myProjects = Project.objects.all().values()
    # limited_projects = myProjects[:3]
    template = loader.get_template('main/home.html')
    context = {
      'myProjects': myProjects,
    }
    return HttpResponse(template.render(context, request))
def details(request, id):
  myProject = Project.objects.get(id=id)
  template = loader.get_template('main/details.html')
  context = {
    'myProject': myProject,
  }
  return HttpResponse(template.render(context, request))