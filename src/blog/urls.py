from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('category/<category>', views.CatListView.as_view(), name='category'),
    path('search/', views.post_search, name='post_search'),
    path('<slug:post>/', views.post_single, name='post_single'),

]