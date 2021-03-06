from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/<str:id>', views.profile, name='profile'),
    path('update/<str:id>', views.user_update, name='update'),
    path('exceltest/', views.export_excel_test, name='exceltest'),
]
