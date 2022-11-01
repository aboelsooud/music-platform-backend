from django.urls import path

from . import views

albums = views.AlbumApi.as_view({
    'get' : 'list',
    'post' : 'create'
})

manualfiltering = views.AlbumApiManuaFiltering.as_view({
    'get' : 'list',
})

urlpatterns = [
    path('', albums, name='albums'),
    path('manual/', manualfiltering, name='albums filtering'),
]
