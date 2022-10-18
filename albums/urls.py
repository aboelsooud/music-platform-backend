from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='albums'),
    path('create/', views.create_album, name='create album'),
]
