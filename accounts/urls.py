from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path("register/", views.user_registration, name = "register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

]    