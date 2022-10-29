from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='artists'),
    path('create/', views.create_artist, name='create artist'),
]
