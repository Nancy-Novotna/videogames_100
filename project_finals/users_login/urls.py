from django.urls import path
from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("user_steam/", views.profile, name="user_steam"),
]