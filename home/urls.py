from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('contact',views.contact,name='Contact'),
    path('about',views.about,name='About'),
    path('search',views.search,name='Search'),
]