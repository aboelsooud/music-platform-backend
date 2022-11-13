from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='albums'),
    path('create/', views.CreateAlbumView.as_view(), name='create album'),
]
