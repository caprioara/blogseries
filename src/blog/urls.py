from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
]