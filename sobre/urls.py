from django.urls import path
from .views import sobre_view

urlpatterns = [
    path('', sobre_view, name='sobre'),
]
