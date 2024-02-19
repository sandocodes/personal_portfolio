from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# category
class Category(models.Model):
    # id field will automatically be generated each time a new category is created
    category_name = models.CharField(max_length=255)


# Blog Post
class Post(models.Model):
    # id field will automatically be generated each time a new blog post is created
    title = models.CharField(max_length=255, unique=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    post_image = models.ImageField(upload_to="assets/blog_images")

