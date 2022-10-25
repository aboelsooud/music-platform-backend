from re import template
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArtistApiView.as_view(), name= "artists")
]
