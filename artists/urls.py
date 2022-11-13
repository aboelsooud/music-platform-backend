from re import template
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='artists'),
    path('create/', views.CreateArtistView.as_view(), name='create artist'),
]
