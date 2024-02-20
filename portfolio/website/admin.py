from django.contrib import admin
from .models import Category, BlogPost, Project

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Project)