from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('course', views.course, name='course'),
    path('detail', views.detail, name='detail'),
    path('feature', views.feature, name='feature'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
]
