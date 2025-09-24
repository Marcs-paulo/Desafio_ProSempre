from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_detail, name='noticias_home'),           # página inicial
    path('<slug:slug>/', views.post_detail, name='post_detail'), # post específico
]
