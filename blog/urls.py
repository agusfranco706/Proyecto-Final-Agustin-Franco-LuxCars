from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('pages/', views.blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('pages/create/', views.blog_create, name='blog_create'),
    path('pages/<int:blog_id>/edit/', views.blog_update, name='blog_update'),
    path('pages/<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
]
