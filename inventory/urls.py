from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory'),
    path('package/', views.package, name='package'),
]
