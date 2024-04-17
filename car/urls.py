from django.contrib import admin
from django.urls import include, path
from car import views

urlpatterns = [
path('', views.home, name='home'),
path('account/', views.login, name='login'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('create/', views.create, name='create'),
path('home/', views.home, name='index'),
path('rent/', views.rent, name='rent'),
path('product/', views.product, name='product')

]

