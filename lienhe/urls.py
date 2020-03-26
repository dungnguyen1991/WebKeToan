from django.urls import path
from . import views

urlpatterns = [
    path('', views.lien_he, name = 'lien_he'),
]