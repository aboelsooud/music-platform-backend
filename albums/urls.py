from django.urls import path

from . import views

albums = views.AlbumApi.as_view({
    'get' : 'list',
    'post' : 'create'
})

urlpatterns = [
    path('', albums, name='albums'),
]
