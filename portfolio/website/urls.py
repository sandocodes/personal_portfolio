from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home_page, name='website_home'),
    path('about-me/', views.about_page, name='website_about_page'),
    path('projects/', views.projects_page, name='website_projects_page'),
    path('blog/', views.blog_section_page, name='website_blog_section_page'),
    path('contact-me/', views.contact_page, name='website_contact_page'),
    # path('blog', views., name=''),
    # path('blog', views., name=''),
]


urlpatterns += staticfiles_urlpatterns()
