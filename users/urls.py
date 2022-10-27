from django.urls import path

from . import views

user_detail = views.UserViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
}) 

urlpatterns = [
    path('<int:pk>/', user_detail, name= "user detail"),
]
