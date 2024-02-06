from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def home_page(request):
    page_name = 'home.html'
    return render(request, page_name, {'title': 'Welcome Page'})


# about view
def about_page(request):
    # template = loader.get_template('about_page.html')
    page_name = 'about_page.html'
    return render(request, page_name, {'title': 'About Page'})


# projects view
def projects_page(request):
    page_name = 'projects_page.html'
    return render(request, page_name, {'title': 'Projects Page'})


# blog seciton view - Will render blog posts later
def blog_section_page(request):
    page_name = 'blog_section.html'
    return render(request, page_name, {'title': 'Blog - Weekly 5 Minutes Read'})

