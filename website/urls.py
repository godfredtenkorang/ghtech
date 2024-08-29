from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('blog', views.blog, name='blog'),
    path('blogDetail', views.blogDetail, name='blogDetail'),
    path('contact', views. contact, name=' contact'),
    path('ourWork', views.ourWork, name='ourWork'),
    path('service', views.service, name='service'),
]