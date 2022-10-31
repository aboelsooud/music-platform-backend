from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlbumApi.as_view(), name='albums'),
]
