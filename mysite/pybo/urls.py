from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index/', views.index, name = 'index'),
    path('highlight/', views.highlight, name = 'highlight'),
    path('rank/', views.rank, name = 'rank'),
    path('record/', views.record, name = 'record')
]