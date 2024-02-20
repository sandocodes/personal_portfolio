from django.db import models
from ckeditor.fields import RichTextField

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
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def snippet(self):
        return self.body[:150] + "..."


# Programming Language
class Language(models.Model):
    programming_language = models.CharField(max_length=255, unique=True)


# Projects
class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    descritption = RichTextField(blank=False, null=False)
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
    