from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


# about view
def about_page(request):
    template = loader.get_template('about_page.html')
    return HttpResponse(template.render())


# projects view
def projects_page(request):
    template = loader.get_template('projects_page.html')
    return HttpResponse(template.render())


# blog seciton view
def blog_section_page(request):
    template = loader.get_template('blog_section.html')
    return HttpResponse(template.render())

