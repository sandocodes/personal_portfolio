from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

# category
class Category(models.Model):
    # id field will automatically be generated each time a new category is created
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


# Blog Post
class BlogPost(models.Model):
    # id field will automatically be generated each time a new blog post is created
    title = models.CharField(max_length=255, unique=True)
    body = CKEditor5Field(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    blog_snippet = CKEditor5Field(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def snippet(self):
        return self.blog_snippet


# Programming Language
class Language(models.Model):
    prog_language_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.prog_language_name


# Projects
class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    descritption = CKEditor5Field(blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    project_url = models.URLField(max_length=255, null=True)
    languages = models.ManyToManyField("Language", related_name="projects", null=True)


    def __str__(self) -> str:
        return self.name
    

    def snippet(self):
        return self.descritption[:100] + "..."
    