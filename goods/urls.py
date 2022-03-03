from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.goods_list, name='goods'),
]
