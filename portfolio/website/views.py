from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost



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
    posts = BlogPost.objects.order_by('-date_created')
    page_name = 'blog_section.html'
    return render(request, page_name, {'title': 'Blog - Weekly 5 Minutes Read', 'posts': posts})

# Blog Detail Page
def blog_detail_page(request, slug):
    page_name = 'blog_detail.html'
    article = BlogPost.objects.get(slug=slug)
    return render(request, page_name, {'blog': article})


# Contact seciton view 
def contact_page(request):
    page_name = 'contact.html'
    return render(request, page_name, {'title': 'Blog - Weekly 5 Minutes Read'})

