from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api/featured-posts/', views.featured_posts_api, name='featured_posts_api'),
]
