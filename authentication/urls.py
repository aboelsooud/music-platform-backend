from re import template
from django.urls import path
from knox import views as knox_views

from . import views

urlpatterns = [
    path('login/', views.LoginApiView.as_view(), name= "Login"),
    path('logout/', knox_views.LogoutView.as_view(), name="Logout"),
]
