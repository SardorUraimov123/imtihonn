from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('guard/', views.guard, name='guard'),
    path('contact/', views.contact, name='contact')
]
