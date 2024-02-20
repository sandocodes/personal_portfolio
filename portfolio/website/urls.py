from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home_page, name='website_home'),
    path('about-me/', views.about_page, name='website_about_page'),
    path('projects/', views.projects_page, name='website_projects_page'),
    path('project/<slug>', views.project_detail_page, name='project_detail_page'),
    path('blog/', views.blog_section_page, name='website_blog_section_page'),
    path('blog/<slug>', views.blog_detail_page, name='blog_detail'),
    path('contact-me/', views.contact_page, name='website_contact_page'),
]


urlpatterns += staticfiles_urlpatterns()
